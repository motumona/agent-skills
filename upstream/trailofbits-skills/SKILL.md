---
name: trailofbits-skills
description: "Hub for the curated Trail of Bits skills collection (trailofbits/skills, CC-BY-SA-4.0) - audit, review, and analysis skills."
---

# Trail of Bits Skills — hub lokal (ditulis Muse, 17 Nov 2026)

Subset kurasi dari library **trailofbits/skills** (GitHub, lisensi CC-BY-SA-4.0). Repo aslinya berisi ~40 plugin dengan puluhan skill; yang dipasang di sini hanya 10 skill yang relevan buat hunting/audit motu (7 awal + 3 dari plugin building-secure-contracts/static-analysis, ditambah 17 Nov 2026). File-file di `skills/` disalin verbatim dari repo (terverifikasi `diff -r` identik dengan sumber, commit `149d7b21`, 12 Nov 2026).

Pintu masuk: **audit-context-building** untuk memahami codebase sebelum berburu bug, lalu **entry-point-analyzer** untuk memetakan attack surface, **fp-check** untuk memverifikasi temuan, **variant-analysis** untuk mencari varian bug yang sama, dan **cvss-scoring** untuk memberi skor severity.

## Skill terpasang (10)

### Pemahaman & pemetaan audit
- **audit-context-building** — pahami codebase sebelum berburu bug: apa yang diasumsikan tiap fungsi, apa yang dijamin, apa yang bergantung ke tempat lain. Dipakai di awal audit/threat model/review arsitektur, sebelum hunting.
- **entry-point-analyzer** — identifikasi semua entry point yang mengubah state di smart contract (Solidity, Vyper, Solana/Rust, Move, TON, CosmWasm), klasifikasikan per level akses (public, role-restricted, contract-only), dan hasilkan laporan terstruktur. Slither opsional.
- **audit-prep-assistant** — siapkan codebase sendiri sebelum diaudit orang lain: checklist review Trail of Bits, jalankan static analysis, naikkan coverage test, hapus dead code, hasilkan dokumentasi (flowchart, user story, komentar). Dipakai saat menyiapkan repo buat review eksternal — BUKAN buat memahami kode yang mau diaudit (itu audit-context-building).

### Verifikasi & varian
- **fp-check** — verifikasi temuan yang dicurigai secara sistematis untuk membasmi false positive: verdict TRUE POSITIVE / FALSE POSITIVE dengan bukti. Bukan untuk hunting bug baru.
- **variant-analysis** — cari instans lain dari bug yang sudah ditemukan (varian satu root cause di seluruh codebase), termasuk generalisasi ke query CodeQL/Semgrep. Dipakai segera setelah satu bug ditemukan, bukan untuk discovery awal.

### Review & testing
- **differential-review** — review keamanan atas perubahan kode (PR/commit/diff): git blame, blast radius, coverage test, adversarial modeling, laporan markdown.
- **property-based-testing** — tulis, review, dan debug property-based test (Hypothesis, fast-check, proptest, Echidna/Medusa untuk invariansi Solidity).

### Penilaian severity
- **cvss-scoring** — hasilkan vector string CVSS v4.0 dari deskripsi kerentanan + link kalkulator FIRST.org. Tidak menghitung skor numerik sendiri. Satu-satunya file non-markdown: `.calcifier/recipe.py` (recipe Calcifier untuk rendering vector, bukan script yang dijalankan di sini).

### Token & integrasi
- **token-integration-analyzer** — analisis implementasi token (ERC20/ERC721) dan risikonya saat diintegrasikan: cek kesesuaian standar, 20+ pola token aneh (fee-on-transfer, rebasing, missing return value, blocklist), komposisi kontrak, hak owner, analisis scarcity on-chain. Dipakai saat menilai token yang akan diterima/diintegrasikan protokol — langsung relevan buat hunting DeFi (token aneh = kelas bug yang sering dibayar).

### Static analysis
- **semgrep** — scan static analysis Semgrep atas codebase: deteksi bahasa, pilih ruleset (registry + repo pihak ketiga Trail of Bits/0xdea/Decurity), rencana scan WAJIB disetujui dulu (hard gate Step 3), jalankan via `skills/semgrep/scripts/run-scans.sh` (paksa `--metrics=off`), gabung output ke SARIF via `skills/semgrep/scripts/merge_sarif.py`. Satu-satunya skill di hub ini yang membawa script eksekusi (`.sh` + 2 `.py`, sudah dibaca penuh — bersih, lihat butir 6). **Prasyarat: binary `semgrep` BELUM terpasang di VM** — instal versi OSS gratis dulu sebelum skill ini bisa jalan; Semgrep Pro (berbayar) TIDAK dipakai.

## Yang TIDAK terpasang (sisa 2 plugin)

- **building-secure-contracts** — BUKAN satu skill, melainkan plugin berisi 11 skill. 2 di antaranya SUDAH dipasang 17 Nov 2026 (`token-integration-analyzer`, `audit-prep-assistant` — lihat di atas). Sisanya belum: 6 vulnerability-scanner per chain (algorand/cairo/cosmos/solana/substrate/ton), `code-maturity-assessor`, `guidelines-advisor`, `secure-workflow-guide`.
- **static-analysis** — BUKAN satu skill, melainkan plugin berisi 3 skill. 1 SUDAH dipasang 17 Nov 2026 (`semgrep` — lihat di atas). Sisanya belum: `codeql`, `sarif-parsing` (query CodeQL sebagian sudah tercakup lewat `variant-analysis` — resources/codeql + resources/semgrep).

## Catatan lokal — baca dulu sebelum pakai

1. **HANYA untuk target yang diizinkan.** Skill-skill ini dipakai hanya untuk program bounty resmi yang motu kerjakan (Ethereum Foundation, Safe, Relay, CoW, Spark, Across) dan target lain yang motu perintahkan eksplisit. Aturan pemilik (motu) MENANG atas doktrin agresif bawaan skill — lihat `LOCAL-NOTES.md`.
2. **Skill = panduan teks, tidak jalan otomatis.** Tidak ada hook, installer, atau perintah yang dieksekusi sendiri; semua langkah dijalankan Muse saat hunting, dan submit tetap butuh persetujuan motu (teks laporan persis + KYC).
3. **Perintah/agents/workflow plugin TIDAK ikut terpasang.** Beberapa SKILL.md merujuk ke perintah plugin (`/audit-context-building:audit-context`, `/variant-analysis:variants`, `/diff-review`), subagent (`audit-context-building:function-analyzer`, `differential-review:adversarial-modeler`, `fp-check` agents), workflow `.js`, dan eval — semua itu tinggal di repo upstream dan tidak disalin. Pakai metodologinya; jangan harapkan perintah/tool yang merujuk plugin bisa jalan apa adanya.
4. **Frontmatter `allowed-tools` mengacu ke Claude Code.** Beberapa skill mencantumkan `allowed-tools` (mis. `Workflow`, `Task`, `AskUserQuestion`, `TaskCreate`) yang merupakan tool Claude Code, bukan Muse. Abaikan daftar itu; pakai sebagai panduan, bukan batasan tool.
5. **Jangan dobel dengan skill bug-hunting.** Skill custom `bug-hunting` (workflow EF/HyperLiquid + 7-Question Gate, dibuat 12 Nov 2026) tetap dipakai buat hunting Geth/EF; skill-skill di sini melengkapinya, terutama audit-context-building (pemahaman codebase), fp-check (verifikasi temuan), dan cvss-scoring (skor severity).
6. **Vetting 17 Nov 2026: bersih.** 80 file (48 `.md`, 14 `.yaml`, 9 `.svg`, 5 `.ql`, 3 `.py`, 1 `.sh`), total 466.594 byte, tanpa executable, tanpa hook, tanpa script installer. Grep pola mencurigakan bersih — hit yang ada semuanya jinak: "private keys" hanya teks contoh Heartbleed di cvss-scoring, `getenv`/`os.environ` hanya pola query deteksi di CodeQL/Semgrep variant-analysis (bukan exfil), URL eksternal hanya first.org (kalkulator CVSS resmi), w3.org (namespace SVG), dan secure-contracts.com (situs Trail of Bits sendiri). Satu-satunya `.py` awal (`cvss-scoring/.calcifier/recipe.py`) dibaca penuh: hanya merender vector CVSS, tanpa network/shell/secret. **Tambahan 17 Nov 2026 (3 skill baru, 17 file, 177.063 byte):** `semgrep/scripts/run-scans.sh` dibaca penuh — hanya menjalankan binary `semgrep` lokal (wajib `--metrics=off`, tanpa telemetri) + `git clone --depth 1` ruleset dari URL https yang sudah divalidasi di file rencana; tanpa `curl|sh`, tanpa secret, tanpa upload hasil ke mana pun. `semgrep/scripts/merge_sarif.py` dibaca penuh — Python murni stdlib (json/sys/pathlib), tanpa subprocess, tanpa network; test-nya sendiri menegaskan tidak ada shell-out. `test_merge_sarif.py` hanya test pytest lokal. URL baru di 3 skill: repo ruleset Semgrep publik (github.com/trailofbits, 0xdea, Decurity, dll), semgrep.dev (dokumen), json.schemastore.org (skema SARIF). Semgrep Pro disebut sebagai opsional berbayar — TIDAK dipakai (lihat LOCAL-NOTES).
