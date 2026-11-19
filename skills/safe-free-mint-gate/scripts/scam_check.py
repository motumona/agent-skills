#!/usr/bin/env python3
"""Cek URL / teks sebelum connect wallet, login, atau klik link.

  scam_check.py <url> [--project NamaProject]
  scam_check.py --text "isi pesan/halaman"
  scam_check.py --add-block evil-domain.xyz
  scam_check.py --add-trusted galxe.com

Verdict: ok | warn | block. Heuristik saja — 'ok' bukan jaminan, 'block' wajib dipatuhi.

Diadaptasi untuk safe-free-mint-gate (motu) dari airdrop-agent v0.3.0
(Setya Mickala, MIT): dibuat mandiri, tanpa dependensi paket upstream.
Daftar domain lokal ada di data/ skill ini (blocklist.txt,
trusted_domains.txt, project_domains.txt). Ditambah domain yang relevan
buat motu: bscscan.com, element.market, datt.my.
"""
from __future__ import annotations

import argparse
import json
import logging
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
BLOCK_FILE = DATA_DIR / "blocklist.txt"
TRUST_FILE = DATA_DIR / "trusted_domains.txt"
PROJECTS_FILE = DATA_DIR / "project_domains.txt"

log = logging.getLogger("scam_check")


def out(obj) -> None:
    print(json.dumps(obj, indent=2, ensure_ascii=False))


KNOWN = ["metamask.io", "rabby.io", "uniswap.org", "opensea.io", "galxe.com", "zealy.io", "layer3.xyz",
         "intract.io", "taskon.xyz", "guild.xyz", "collab.land", "debank.com", "etherscan.io", "basescan.org",
         "arbiscan.io", "jup.ag", "phantom.app", "pancakeswap.finance", "lido.fi", "eigenlayer.xyz",
         "telegram.org", "discord.com", "x.com", "twitter.com", "linea.build", "zksync.io", "scroll.io",
         "optimism.io", "arbitrum.io", "base.org", "chain.link", "alchemy.com", "infura.io", "quicknode.com",
         "coinbase.com", "binance.com", "okx.com", "bybit.com",
         "bscscan.com", "element.market", "datt.my"]
DEFAULT_TRUSTED = set(KNOWN) | {"t.me", "web.telegram.org", "discord.gg", "google.com", "github.com",
                                "faucets.chain.link", "cloud.google.com", "faucet.polygon.technology"}
RISKY_TLDS = {"xyz-claim", "top", "click", "cfd", "sbs", "buzz", "rest", "monster", "icu", "cyou", "lol",
              "quest", "beauty", "hair", "bond", "zip", "mov"}
PATH_FLAGS = re.compile(r"(claim-?airdrop|validate|rectify|sync-?wallet|wallet-?connect-?fix|restore|recover|"
                        r"migration|seed|phrase|revoke-all|airdrop-?checker)", re.I)
TEXT_FLAGS = [
    (re.compile(r"(seed|recovery|secret|mnemonic)\s*(phrase|words?)|private\s*key", re.I), "block",
     "meminta seed phrase / private key"),
    (re.compile(r"(validate|sync|rectify|restore)\s+(your\s+)?wallet", re.I), "block", "pola 'validate/sync wallet'"),
    (re.compile(r"send\s+\d.*(to|ke)\s+(receive|get|double)|kirim.*(dapat|dobel)", re.I), "block",
     "kirim dulu untuk dapat hadiah"),
    (re.compile(r"(urgent|last chance|only \d+ (minutes|hours) left|segera|terakhir)", re.I), "warn", "tekanan waktu"),
    (re.compile(r"(support|admin|moderator).{0,40}(dm|direct message|chat me)", re.I), "warn",
     "'admin/support' ngajak DM"),
    (re.compile(r"(claim|klaim).{0,30}(airdrop|reward|token).{0,40}(connect|sambung)", re.I), "warn",
     "klaim airdrop + connect wallet (cek domain resmi!)"),
    (re.compile(r"(pay|bayar).{0,30}(gas|fee|biaya).{0,30}(to|untuk).{0,20}(claim|unlock|withdraw)", re.I), "block",
     "bayar biaya untuk unlock/klaim"),
]


def _load(path, default=()):
    if not path.exists():
        return set(default)
    return {l.strip().lower() for l in path.read_text().splitlines()
            if l.strip() and not l.strip().startswith("#")}


def _lev(a: str, b: str) -> int:
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


def _root(host: str) -> str:
    parts = host.split(".")
    return ".".join(parts[-2:]) if len(parts) >= 2 else host


def _match(host: str, dom: str) -> bool:
    return host == dom or host.endswith("." + dom)


def _project_domains(name: str) -> set[str]:
    """Domain resmi proyek dari data/project_domains.txt (format: nama domain1 domain2)."""
    if not PROJECTS_FILE.exists():
        return set()
    for line in PROJECTS_FILE.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split()
        if parts and parts[0].lower() == name.lower():
            return {d.lower() for d in parts[1:]}
    return set()


def check_url(url: str, project: str | None = None) -> dict:
    reasons, level = [], "ok"
    order = {"ok": 0, "warn": 1, "block": 2}

    def bump(lv, why):
        nonlocal level
        if order[lv] > order[level]:
            level = lv
        reasons.append(why)

    u = urlparse(url if "://" in url else "https://" + url)
    host = (u.hostname or "").lower()
    host = host[4:] if host.startswith("www.") else host
    if u.scheme != "https":
        bump("warn", "bukan https")
    if not host:
        return {"verdict": "block", "reasons": ["URL tidak valid"], "host": host}
    blocked = _load(BLOCK_FILE)
    trusted = _load(TRUST_FILE, DEFAULT_TRUSTED) | DEFAULT_TRUSTED
    if any(_match(host, b) for b in blocked):
        bump("block", "domain ada di blocklist")
    if "xn--" in host:
        bump("block", "domain punycode (huruf mirip)")
    if re.fullmatch(r"[\d.]+", host):
        bump("block", "URL berupa IP")
    tld = host.rsplit(".", 1)[-1]
    if tld in RISKY_TLDS:
        bump("warn", f"TLD berisiko .{tld}")
    if host.count("-") >= 3 or len(host) > 40:
        bump("warn", "domain panjang/banyak tanda hubung")
    if PATH_FLAGS.search(u.path + "?" + (u.query or "")):
        bump("warn", "path mengandung kata khas phishing")
    is_trusted = any(_match(host, t) for t in trusted)
    if not is_trusted:
        rname = _root(host).split(".")[0]
        for k in KNOWN:
            kname = k.split(".")[0]
            if len(kname) < 5:
                continue
            dist = _lev(rname, kname)
            if 0 < dist <= (1 if len(kname) <= 6 else 2):
                bump("block", f"mirip domain resmi {k} (lookalike)")
                break
            if len(kname) >= 6 and kname in host:
                if tld in RISKY_TLDS or re.search(r"(claim|airdrop|reward|bonus|gift|drop|verify|support)", host):
                    bump("block", f"nama brand '{kname}' + kata umpan di domain palsu")
                else:
                    bump("warn", f"memakai nama '{kname}' tapi bukan {k} — pastikan ini domain resmi")
                break
    if project:
        doms = _project_domains(project)
        if not doms:
            bump("warn", f"project '{project}' tidak punya URL resmi di project_domains.txt")
        elif not any(_match(host, d) for d in doms) and not is_trusted:
            bump("warn", f"bukan domain resmi {project} ({', '.join(sorted(doms))})")
    return {"verdict": level, "host": host, "trusted": is_trusted, "reasons": reasons or ["tidak ada tanda bahaya"]}


def check_text(text: str) -> dict:
    order = {"ok": 0, "warn": 1, "block": 2}
    reasons, level = [], "ok"
    for rx, lv, why in TEXT_FLAGS:
        if rx.search(text):
            reasons.append(why)
            level = max(level, lv, key=order.get)
    for url in re.findall(r"https?://[^\s\"'<>)]+", text)[:10]:
        r = check_url(url)
        if r["verdict"] != "ok":
            reasons.append(f"{r['host']}: {r['verdict']} ({'; '.join(r['reasons'])})")
            level = max(level, r["verdict"], key=order.get)
    return {"verdict": level, "reasons": reasons or ["tidak ada tanda bahaya"]}


def main():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(level=logging.INFO, stream=sys.stderr)
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("url", nargs="?")
    p.add_argument("--project")
    p.add_argument("--text")
    p.add_argument("--add-block")
    p.add_argument("--add-trusted")
    a = p.parse_args()
    if a.add_block:
        with open(BLOCK_FILE, "a") as f:
            f.write(a.add_block.lower().strip() + "\n")
        out({"blocked": a.add_block})
    elif a.add_trusted:
        with open(TRUST_FILE, "a") as f:
            f.write(a.add_trusted.lower().strip() + "\n")
        out({"trusted": a.add_trusted})
    elif a.text:
        out(check_text(a.text))
    elif a.url:
        res = check_url(a.url, a.project)
        log.info("scam_check %s -> %s", a.url, res["verdict"])
        out(res)
    else:
        p.print_help()


if __name__ == "__main__":
    main()
