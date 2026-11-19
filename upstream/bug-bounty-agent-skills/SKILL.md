---
name: bug-bounty-agent-skills
description: "Hub for the curated bug-bounty-agent-skills collection (murrtada/bug-bounty-agent-skills, MIT) - recon, hunting, verification, and report skills for official bug bounty programs."
---

# Bug Bounty Agent Skills — hub lokal (ditulis Muse, 17 Nov 2026)

Subset kurasi dari library **murrtada/bug-bounty-agent-skills** (GitHub, lisensi MIT, turunan Agentic-Bug-Hunter karya Awarexone). Repo aslinya berisi 93 skill; yang dipasang di sini hanya 27 yang relevan buat hunting motu — 93 skill penuh terlalu berat dan sebagian besar di luar scope (red-team enterprise, mobile pentest, VPN/Okta, dsb). File-file di `skills/` disalin verbatim dari repo, kecuali 9 file keluarga `bb-*` yang di repo aslinya TIDAK punya frontmatter — ke 9 file itu ditambahkan frontmatter minimal (name + description saja, isi tidak diubah) supaya bisa dipakai sebagai skill di Muse.

Pintu masuk: **bug-bounty** untuk full campaign loop (recon → belajar dari laporan yang sudah diungkap → hunting → verifikasi → lapor), atau **bb-methodology** untuk framework 5 fase yang berdiri sendiri.

## Skill terpasang (27)

### Orkestrasi & metodologi
- **bug-bounty** — workflow lengkap: recon, pre-hunt learning dari laporan yang sudah diungkap, hunting, verifikasi, dan pelaporan.
- **bb-methodology** — orkestrator utama, gabungan framework 5 fase; dipakai di awal sesi hunting atau saat ganti target.
- **hunt-dispatch** — loader skill-set untuk orkestrator /hunt: fingerprint target, pilih skill serangan yang tepat.
- **recon-scope-triage** — triase hasil recon: pisahkan aset asli target dari noise sebelum testing.
- **bb-recon** — metodologi discovery + perintah tool: enumerasi subdomain, live host, fingerprinting.

### Web3 (inti hunting motu)
- **web3-audit** — audit smart contract: 10 kelas bug DeFi (accounting desync, access control, incomplete path, off-by-one, oracle, ERC4626, reentrancy, flash loan, signature replay, proxy), pre-dive kill signals, template PoC Foundry, pola grep tiap kelas, contoh Immunefi yang beneran dibayar.
- **meme-coin-audit** — audit meme coin/token: deteksi rug pull (honeypot, hidden mint, manipulasi fee, LP lock bypass), analisis token SPL Solana.

### Per kelas bug web/API
- **hunt-xss** — XSS, dibangun dari 174 laporan bug bounty publik.
- **hunt-sqli** — SQLi + NoSQLi, dari 12 laporan publik.
- **hunt-rce** — RCE, dari 67 laporan publik.
- **hunt-ssrf** — SSRF, dari 15 laporan publik (termasuk SSRF metadata AWS). 17 Nov 2026: dilipat 2 bagian tambahan dari Claude-BugHunter (bypass encoding base64/double-encode + path-normalization/semicolon) — isi file kini identik dengan versi Claude-BugHunter kecuali frontmatter.
- **hunt-idor** — IDOR, dari 26 laporan publik.
- **hunt-graphql** — kerentanan GraphQL (IDOR via node()/GID, mutation IDOR).
- **hunt-race-condition** — race condition, termasuk serangan single-packet HTTP/2 modern.
- **bb-api** — referensi testing API & GraphQL (misconfig, WebSocket).
- **bb-authz** — referensi testing AuthN/AuthZ (IDOR, broken access control, JWT, OAuth, auth bypass).
- **bb-logic** — referensi testing business-logic & race condition.
- **bb-cloud** — referensi testing cloud/container yang terjangkau web (SSRF, metadata cloud/IMDS, review config, secret discovery).
- **bb-ai** — referensi testing keamanan AI/LLM (prompt injection, indirect prompt injection, RAG/vector).

### Recon & arsenal
- **web2-recon** — pipeline recon web2: subdomain, live host, crawling URL, wayback/gau.
- **security-arsenal** — payload, tabel bypass, wordlist, pola gf, daftar bug yang selalu ditolak, tabel valid-bersyarat-dengan-chain.

### Validasi & pelaporan
- **triage-validation** — validasi temuan sebelum menulis laporan: 7-Question Gate + 4 gerbang pra-submit + daftar selalu-ditolak.
- **bb-verify** — triase kandidat & disiplin bukti: evidence manifest, apa yang dihitung sebagai bukti.
- **evidence-hygiene** — disiplin capture bukti & redaksi PoC: protokol redaksi cookie, apa yang dimask.
- **report-writing** — penulisan laporan buat H1/Bugcrowd/Intigriti/Immunefi: template, nada manusiawi, impact-first, CVSS 3.1, formula judul.
- **bb-report** — disiplin pelaporan: draft laporan untuk disubmit manusia; jangan pernah submit langsung.
- **bb-handoff** — crafting tugas manual-test: ubah temuan jadi tugas hand-off untuk verifikasi manusia.

## Catatan lokal — baca dulu sebelum pakai

1. **HANYA untuk target yang diizinkan.** Skill-skill ini dipakai hanya untuk program bounty resmi yang motu kerjakan (Ethereum Foundation, Safe, Relay, CoW, Spark, Across) dan target lain yang motu perintahkan eksplisit. Jangan pernah dipakai buat testing tanpa izin — itu ilegal dan melanggar syarat platform.
2. **Skill = panduan teks, tidak jalan otomatis.** Tidak ada script, hook, atau perintah yang dieksekusi sendiri; semua langkah dijalankan Muse saat hunting, dan submit tetap butuh persetujuan motu (teks laporan + KYC).
3. **Keluarga `bb-*` berasumsi ada sistem `bb-ops` yang TIDAK terpasang.** File bb-recon, bb-verify, bb-report, bb-handoff, bb-logic, bb-api, bb-authz, bb-cloud, dan bb-ai merujuk ke `bb-ops/lib/scope.py` dan `bb-ops/playbooks/*.yaml` dari sistem upstream Agentic-Bug-Hunter — file-file itu tidak ada di repo ini dan tidak ikut dipasang. Pakai metodologinya; jangan harapkan perintah/tool yang merujuk bb-ops bisa jalan apa adanya.
4. **Jangan dobel dengan skill bug-hunting.** Skill custom `bug-hunting` (workflow EF/HyperLiquid + 7-Question Gate, dibuat 12 Nov 2026) tetap dipakai buat hunting Geth/EF; skill-skill di sini melengkapinya, terutama web3-audit (DeFi/Immunefi) dan hunt-* (web/API).
5. **Vetting 17 Nov 2026: bersih.** 27 file, semuanya `.md` murni (544 KB), tanpa script/hook. Grep pola mencurigakan bersih — 2 hit "PRIVATE KEY" hanya contoh teks dokumentasi (apa yang dicari saat recon), host eksternal semua placeholder/demo (target.com, evil.com, attacker.com, 169.254.169.254 untuk contoh SSRF) atau situs resmi (hackerone.com, github.com, portswigger.net). Tidak ada secret hardcode, tidak ada host exfil.
