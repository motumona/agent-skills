---
name: bugskill-ai
description: Hub for three bug-hunting skills (URL parser confusion and SSRF filter bypass, stack-bounds format auditing, OTP brute-force testing) plus a HackerOne public-reports dataset with search tools. Use when hunting those three vulnerability classes on in-scope bug bounty targets.
---

> CATATAN LOKAL (Muse, 24 Nov 2026): Hub tipis — dibuat 24 Nov 2026 karena folder bugskill-ai tidak punya SKILL.md. Aturan yang sama seperti sub-skillnya: hanya target resmi program bug bounty yang AKTIF dan dalam scope, dengan izin tertulis program. JANGAN submit laporan apa pun tanpa persetujuan eksplisit motu atas isi laporan persisnya. Hanya jalur submit GRATIS; jangan bayar apa pun, jangan buat akun, jangan KYC.

# Bugskill-AI

Tiga skill berburu bug + dataset laporan publik HackerOne. Buka sub-skill yang relevan — hub ini hanya peta jalan, bukan pengganti isi tiap skill.

## Sub-skill

1. **url-parser-confusion-testing** — `url-parser-confusion-testing/SKILL.md`. Mendeteksi bypass filter SSRF dan inkonsistensi parsing URL (triple-slash, backslash, delimiter ter-encode, userinfo, bentuk IP numerik, IPv4-mapped IPv6). Skrip: `scripts/url_parser_diff.py`. Mereproduksi HackerOne #3923212 (curl URL API triple-slash).
2. **stack-bounds-format-auditing** — `stack-bounds-format-auditing/SKILL.md`. Mendeteksi dan mengaudit stack buffer overflow dari aritmetika bounds yang salah di string formatting dan memory copy (snprintf, sprintf, strncpy, memcpy). Skrip: `scripts/fmt_bounds_audit.py`. Mereproduksi HackerOne #2551512 (Nintendo NEX StationURL::Format).
3. **otp-bruteforce-testing** — `otp-bruteforce-testing/SKILL.md`. Mendeteksi, memvalidasi, dan mengeksploitasi kerentanan brute-force OTP di verifikasi telepon/email, MFA, reset password, dan konfirmasi transaksi. Skrip: `scripts/otp_bruteforce.py`.

## Dataset + perkakas pencarian

- `hackerone_public_reports.json` — dataset laporan publik HackerOne (~14 MB).
- `hackerone_public.py` + `search_reports.py` — baca dan cari di dataset di atas.
- `requirements.txt` — dependensi Python untuk perkakas di atas.
- `LICENSE-upstream` — lisensi dataset/skrip (periksa sebelum distribusi ulang).
