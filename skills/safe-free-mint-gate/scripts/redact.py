"""Secret redaction for logs and any text that may reach the LLM.

- Masks values of sensitive env vars currently loaded.
- Masks patterns that look like private keys, seeds, tokens, OTP-bearing URLs.

Diadaptasi untuk safe-free-mint-gate (motu) dari airdrop-agent v0.3.0
(Setya Mickala, MIT): dibuat mandiri, tanpa dependensi paket upstream.
Pola dan perilaku sama seperti aslinya.

Usage: some_command | python3 scripts/redact.py   (sanitize any output before showing it)
"""
from __future__ import annotations

import logging
import os
import re

SENSITIVE_ENV_HINTS = ("KEY", "SECRET", "TOKEN", "PASSWORD", "PASS", "HASH", "SEED", "MNEMONIC", "SESSION", "COOKIE")

PATTERNS = [
    # bare 64-hex (no 0x) = typical private key export. 0x+64hex is usually a tx hash, so only mask
    # it when the surrounding text says key/secret/private.
    (re.compile(r"(?<![0-9a-fA-Fx])[a-fA-F0-9]{64}(?![0-9a-fA-F])"), "[REDACTED_HEX64]"),
    (re.compile(r"(?i)((?:priv(?:ate)?[_ ]?key|secret|pk|seed)[\"']?\s*[:=]\s*[\"']?)0x[a-fA-F0-9]{64}"), r"\1[REDACTED_KEY]"),
    (re.compile(r"\b[1-9A-HJ-NP-Za-km-z]{85,90}\b"), "[REDACTED_B58_KEY]"),    # Solana secret key base58
    (re.compile(r"\b\d{8,10}:[A-Za-z0-9_-]{35}\b"), "[REDACTED_TG_BOT_TOKEN]"),
    (re.compile(r"\b[MNO][A-Za-z\d_-]{23,25}\.[A-Za-z\d_-]{6}\.[A-Za-z\d_-]{27,38}\b"), "[REDACTED_DISCORD_TOKEN]"),
    (re.compile(r'("crypto"\s*:\s*\{).*?(\})', re.S), r"\1[REDACTED_KEYSTORE]\2"),
    (re.compile(r"(?i)(password|passwd|secret|api[_-]?key|token)=([^\s&]+)"), r"\1=[REDACTED]"),
]


_MNEMONIC_RE = re.compile(r"\b(?:[a-z]{3,8}\s+){11,23}[a-z]{3,8}\b")
_BIP39: set[str] | None = None


def _bip39() -> set[str]:
    """Load BIP39 English list shipped with eth_account (fallback: empty set)."""
    global _BIP39
    if _BIP39 is None:
        _BIP39 = set()
        try:
            import eth_account, pathlib
            f = pathlib.Path(eth_account.__file__).parent / "hdaccount" / "wordlist" / "english.txt"
            _BIP39 = set(f.read_text().split())
        except Exception:
            pass
    return _BIP39


def _mask_mnemonic(m: re.Match) -> str:
    words = m.group(0).split()
    wl = _bip39()
    # if wordlist unavailable, be conservative and mask anyway
    if not wl or sum(w in wl for w in words) >= len(words) - 1:
        return "[REDACTED_MNEMONIC]"
    return m.group(0)


def _env_secrets() -> list[str]:
    vals = []
    for k, v in os.environ.items():
        if v and len(v) >= 6 and any(h in k.upper() for h in SENSITIVE_ENV_HINTS):
            vals.append(v)
    return sorted(vals, key=len, reverse=True)


def redact(text: str) -> str:
    if not isinstance(text, str):
        text = str(text)
    for v in _env_secrets():
        text = text.replace(v, "[REDACTED_ENV]")
    for pat, rep in PATTERNS:
        text = pat.sub(rep, text)
    return _MNEMONIC_RE.sub(_mask_mnemonic, text)


class RedactingFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        record.msg = redact(record.getMessage())
        record.args = ()
        return True


if __name__ == "__main__":
    import sys

    # usage: some_command | python redact.py   (sanitize any output before showing the LLM)
    for line in sys.stdin:
        sys.stdout.write(redact(line))
