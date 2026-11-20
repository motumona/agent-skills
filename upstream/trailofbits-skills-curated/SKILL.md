---
name: trailofbits-skills-curated
description: "Hub for the curated Trail of Bits skills-curated collection (trailofbits/skills-curated, CC-BY-SA-4.0) - reviewed audit skills."
---

# Trail of Bits Skills Curated — hub lokal (ditulis Muse, 17 Nov 2026)

Subset kurasi dari library **trailofbits/skills-curated** (GitHub, lisensi repo CC-BY-SA-4.0 — lihat catatan lisensi per skill di bawah). Repo aslinya berisi 31 skill dalam bentuk plugin Claude Code yang sudah di-review Trail of Bits; yang dipasang di sini hanya 3 yang relevan buat hunting motu. File-file di `skills/` disalin verbatim dari repo (terverifikasi identik via `diff -r`); tidak ada installer, hook, atau setup yang dijalankan.

Pintu masuk: **scv-scan** untuk audit smart contract (inti hunting web3 motu), **ffuf-web-fuzzing** untuk fuzzing web target bounty, atau **wooyun-legacy** untuk metodologi testing kerentanan web dari kasus nyata.

## Skill terpasang (3)

### Audit smart contract
- **scv-scan** — audit codebase Solidity untuk 36 kelas kerentanan smart contract (reentrancy, overflow, access control, signature replay, proxy, dsb) lewat workflow 4 fase: muat cheatsheet → sweep codebase → validasi mendalam → lapor. Dilengkapi 37 file referensi (CHEATSHEET + 1 file per kelas bug). Asal: kadenzipfel/scv-scan.

### Web fuzzing
- **ffuf-web-fuzzing** — panduan pakai ffuf (Fuzz Faster U Fool) untuk pentest resmi: directory discovery, enumerasi subdomain, fuzzing parameter/API, fuzzing terautentikasi via raw request, auto-calibration (`-ac` wajib), analisis hasil. Referensi: template request terautentikasi + panduan pilih wordlist SecLists. Asal: jthack.

### Metodologi kerentanan web
- **wooyun-legacy** — metodologi testing kerentanan web yang disuling dari 88.636 kasus nyata database WooYun (2010–2016): SQL injection, XSS, command execution, file upload, path traversal, unauthorized access, info disclosure, logic flaws. Dilengkapi 14 checklist + 10 file referensi mendalam (termasuk bank-penetration dan telecom-penetration — keduanya DI LUAR scope motu, lihat LOCAL-NOTES.md). Asal: tanweai / kontributor wooyun-legacy.

## Lisensi

- Lisensi repo induk: **CC-BY-SA-4.0** (file `LICENSE` di root repo).
- Lisensi per plugin berbeda: **ffuf-web-fuzzing = MIT**, **wooyun-legacy = CC-BY-NC-SA-4.0** (non-komersial — pemakaian motu untuk hunting bounty pribadi bukan komersial, jadi aman), **scv-scan = tanpa file LICENSE sendiri** (ikut lisensi repo induk).
- Atribusi: Trail of Bits (kurator), kadenzipfel (scv-scan), jthack (ffuf-web-fuzzing), tanweai (wooyun-legacy).

## Catatan lokal — baca dulu sebelum pakai

1. **Aturan motu MENANG atas doktrin bawaan skill.** Lihat `LOCAL-NOTES.md` — probe tanpa izin / wild mode DILARANG, hanya target program resmi, tanpa submit tanpa persetujuan teks laporan persis, jalur gratis saja, hunting read-only kecuali PoC disetujui.
2. **Skill = panduan teks, tidak jalan otomatis.** Tidak ada script, hook, atau perintah yang dieksekusi sendiri; semua langkah dijalankan Muse saat hunting.
3. **Jangan dobel dengan skill bug-hunting.** Skill custom `bug-hunting` (workflow EF/HyperLiquid + 7-Question Gate, dibuat 12 Nov 2026) dan hub `bug-bounty-agent-skills` (27 skill, 17 Nov 2026) tetap dipakai; skill-skill di sini melengkapinya — terutama scv-scan (audit Solidity terstruktur, 36 kelas) dan ffuf-web-fuzzing (fuzzing web) serta wooyun-legacy (checklist per kelas bug dari kasus nyata).
4. **Kebutuhan eksternal:** scv-scan dan wooyun-legacy tidak butuh apa pun selain akses baca ke kode/target. ffuf-web-fuzzing butuh binary `ffuf` terpasang (`brew install ffuf` / `go install github.com/ffuf/ffuf/v2@latest`) dan wordlist SecLists (`/opt/SecLists/...` atau unduh dari github.com/danielmiessler/SecLists). Tidak ada API key / akun berbayar yang dibutuhkan.
5. **Vetting 17 Nov 2026: bersih.** 66 file, semuanya `.md` murni (420.384 byte), tanpa script/hook/binary. `diff -r` ke repo sumber: identik untuk ketiga skill. Grep pola mencurigakan: tidak ada secret hardcode, tidak ada host exfil, tidak ada `~/.ssh`/private key sungguhan — semua hit adalah contoh payload dokumentasi (mis. `/etc/passwd` dan `/root/.ssh/id_rsa` sebagai contoh target path-traversal di wooyun-legacy; `curl TARGET:9200` sebagai contoh cek misconfig; `Bearer <redacted>` sebagai placeholder). Semua URL/host di file adalah placeholder (`target.com`, `example.com`, `evil.com`, `attacker.com`, `127.0.0.1`, `metadata.google.internal` sebagai contoh SSRF) atau situs resmi (github.com, solidity.readthedocs.io). Catatan: wooyun-legacy berisi contoh payload ofensif lengkap (brute-force, bypass WAF, dsb) — itu isi metodologinya, bukan malware; pemakaiannya tetap tunduk pada LOCAL-NOTES.md.
