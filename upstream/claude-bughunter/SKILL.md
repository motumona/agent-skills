---
name: claude-bughunter
description: "Hub for the curated Claude-BugHunter collection (elementalsouls/Claude-BugHunter, MIT code / CC BY 4.0 content) - 58 hunting skills for web, cloud, and mobile targets."
---

# Claude-BugHunter — hub lokal (ditulis Muse, 17 Nov 2026)

Subset kurasi dari library **elementalsouls/Claude-BugHunter** (GitHub, kode lisensi MIT, konten skill lisensi CC BY 4.0 — lihat `LICENSE` dan `LICENSE-CONTENT` repo). Repo aslinya berisi 83 skill + 15 slash command; yang dipasang di sini hanya 58 skill yang menambah hal baru buat hunting motu — 25 skill di-skip karena duplikat dengan yang sudah terpasang, di luar scope, atau membawa script eksekusi (rincian di bawah). File-file di `skills/` disalin verbatim dari repo (byte-identical, frontmatter `name` cocok dengan nama folder di semua 58 skill).

Pintu masuk: **hunt-dispatch** (sudah terpasang di hub murrtada) untuk memilih skill serangan berdasarkan fingerprint target, atau langsung ke skill kelas bug yang relevan. Skill red-team enterprise di sini dipakai sebagai referensi metodologi untuk target bounty yang in-scope saja — bukan untuk engagement red-team.

## Skill terpasang (58)

### Red-team enterprise (prioritas — belum ada di hub lain)
- **m365-entra-attack** — rantai serangan M365 / Entra ID: enumerasi user, Smart Lockout, bypass Conditional Access, ROPC + SAML SSO, template Burp/Playwright.
- **okta-attack** — serangan Okta/IdP: enumerasi tenant, bypass kebijakan, rantai ATO via IdP.
- **vmware-vcenter-attack** — serangan VMware vCenter: CVE, eskalasi via layanan manajemen.
- **enterprise-vpn-attack** — serangan VPN enterprise (Fortinet, Pulse, Citrix, Palo Alto, Cisco): CVE, format dump kredensial, bypass auth.
- **cloud-iam-deep** — IAM cloud mendalam (AWS/GCP/Azure): enumerasi peran, privilege escalation, alat graf (AzureHound dsb).
- **supply-chain-attack-recon** — recon supply chain: CI workflow, dependensi, pola `curl | bash`, aksi GitHub tak ter-pin.
- **hunt-k8s** — Kubernetes: etcd tanpa auth, SA token, eskalasi via API.
- **hunt-cicd** — CI/CD: injeksi `${{ }}`, kebocoran tfstate, Pwnrequest.
- **hunt-ldap** — LDAP injection & enumerasi direktori.
- **hunt-saml** — serangan SAML/SSO: XML Signature Wrapping, injeksi komentar NameID, signature stripping, key confusion.
- **hunt-ntlm-info** — NTLM: relay, info disclosure, coercion.
- **hunt-sharepoint** — SharePoint: kebocoran dokumen, bypass akses, rantai via OneDrive/Teams.

### Per kelas bug web/API (baru — belum ada di hub lain)
- **hunt-api-misconfig** — misconfig API: mass assignment, prototype pollution, HTTP verb tampering.
- **hunt-aspnet** — ASP.NET: ViewState, deserialisasi, misconfig.
- **hunt-ato** — account takeover: rantai ATO end-to-end.
- **hunt-auth-bypass** — bypass autentikasi umum.
- **hunt-brute-force** — brute force & rate-limit bypass.
- **hunt-business-logic** — bug business logic.
- **hunt-cache-poison** — cache poisoning.
- **hunt-captcha-bypass** — bypass CAPTCHA.
- **hunt-clickjacking** — clickjacking / UI redress.
- **hunt-cloud-misconfig** — misconfig cloud (bucket, storage, IMDS).
- **hunt-cors** — CORS misconfig.
- **hunt-csrf** — CSRF.
- **hunt-deserialization** — deserialisasi tidak aman.
- **hunt-dom** — DOM XSS & bug sisi klien.
- **hunt-exceptional-conditions** — bug kondisi eksepsional / edge case.
- **hunt-file-upload** — upload file berbahaya.
- **hunt-fintech-graphql** — GraphQL di fintech: IDOR finansial, mutasi sensitif.
- **hunt-forgot-password** — bug alur lupa password / reset token.
- **hunt-grpc** — gRPC: refleksi, IDOR, auth.
- **hunt-host-header** — host header injection.
- **hunt-html-injection** — HTML injection (tanpa eksekusi JS — bedakan dari XSS).
- **hunt-http-smuggling** — HTTP request smuggling.
- **hunt-jwt-crypto** — JWT: alg none, key confusion, kid/jku.
- **hunt-laravel** — Laravel: misconfig, deserialisasi, debug mode.
- **hunt-lfi** — Local File Inclusion.
- **hunt-llm-ai** — keamanan LLM/AI: prompt injection, indirect injection, ASCII smuggling, exfil via tool-use, OWASP Agentic ASI01–ASI10.
- **hunt-mfa-bypass** — bypass MFA/OTP.
- **hunt-misc** — kelas misc dari 225 laporan publik (access control, info disclosure, session/auth).
- **hunt-nextjs** — Next.js: misconfig, RSC, cache.
- **hunt-nodejs** — Node.js: prototype pollution, misconfig.
- **hunt-nosqli** — NoSQL injection.
- **hunt-oauth** — OAuth: redirect_uri, token theft, scope.
- **hunt-open-redirect** — open redirect & chaining ke OAuth theft.
- **hunt-rag-vector** — RAG/vector DB: prompt injection via dokumen, cross-tenant leak.
- **hunt-session** — manajemen session: fixation, hijack, prediksi token.
- **hunt-shadow-api** — shadow API / endpoint tak terdokumentasi.
- **hunt-source-leak** — kebocoran source code: sourcemap, .git, backup.
- **hunt-spa-api** — API aplikasi SPA: endpoint tersembunyi di bundle JS.
- **hunt-springboot** — Spring Boot: actuator, heapdump, misconfig.
- **hunt-ssti** — Server-Side Template Injection.
- **hunt-subdomain** — subdomain takeover: fingerprint provider modern (Azure, Zendesk, Vercel, Fastly, S3).
- **hunt-tls-network** — TLS / network: misconfig, downgrade.
- **hunt-websocket** — WebSocket: auth, IDOR, hijack.
- **hunt-xxe** — XML External Entity.

### Pelaporan & OSINT
- **bugcrowd-reporting** — taktik khusus Bugcrowd (melengkapi report-writing): strategi kategori VRT, override severity manual, template rebuttal klausa OOS, cross-reference temuan berantai.
- **osint-methodology** — metodologi OSINT: asset graph, identity mapping, exposure scoring, CVE/EPSS/KEV, read-only validation.

## Yang di-skip (25) — dedup

### Duplikat isi dengan hub murrtada (18) — body SKILL.md identik atau nyaris identik (diff 0 baris di 16 skill)
bb-methodology, bug-bounty, evidence-hygiene, hunt-dispatch, hunt-graphql, hunt-idor, hunt-race-condition, hunt-rce, hunt-sqli, hunt-xss, meme-coin-audit, recon-scope-triage, report-writing, security-arsenal, triage-validation, web2-recon, web3-audit. Dua pengecualian kecil: **hunt-ssrf** versi Claude-BugHunter punya 2 bagian tambahan (bypass encoding base64/double-encode + path-normalization/semicolon) yang TIDAK ada di versi murrtada — **DILIPAT 17 Nov 2026** ke file murrtada (isi kini identik kecuali frontmatter); **bug-bounty** versi murrtada justru LEBIH kaya (Appendix "Field-Tested Nuggets" 26 baris tidak ada di versi Claude-BugHunter). Keduanya tetap di-skip sebagai skill utuh.

### Duplikat varian (1)
- **bb-local-toolkit** — 73,5 KB, isinya nyaris sama dengan bug-bounty (beda cuma 57 baris diff: tambahan path tool lokal SecLists/ffuf/dalfox/dll). Tidak menambah metodologi baru.

### Di luar scope hunting motu (5)
- **apk-redteam-pipeline**, **ios-redteam-pipeline** — pipeline pentest mobile (APK/IPA, Frida, jadx). Motu hunting web/API + web3, bukan mobile.
- **redteam-mindset**, **redteam-report-template**, **mid-engagement-ir-detection** — doktrin engagement red-team; ketiganya menulis eksplisit "DO NOT use for bug bounty". Tidak berlaku buat program bounty motu.

### Membawa script eksekusi (1)
- **offensive-osint** — SKILL.md-nya merujuk 15 file referensi + 3 script Python (secret_scan.py, h1_reference.py, dashboard.py — web UI localhost). Metodologinya sudah tercakup osint-methodology + web2-recon + hunt-subdomain yang dipasang di sini; script + dashboard tidak ikut dipasang supaya hub ini tetap panduan teks murni (seperti hub murrtada).

## Slash command (15) — TIDAK dipasang
Repo punya 15 file `.md` di `commands/`: autopilot, chain, hunt, intel, memory-gc, pickup, recon, remember, report, scope, surface, token-scan, triage, validate, web3-audit. Formatnya slash command Claude Code (`/hunt target.com`, `/autopilot ... --yolo`) — Muse memakai skill, bukan slash command Claude Code, jadi tidak bisa dipakai. Beberapa juga bergantung pada kode engine repo (`cbh` CLI, `engine/scope.py`, ledger `~/.claude/bughunter/memory/`) dan `install.sh` yang tidak dijalankan. Fungsinya sudah tercakup skill yang terpasang (hunt-dispatch, report-writing, triage-validation, web3-audit, meme-coin-audit).

## Catatan lokal — baca dulu sebelum pakai
1. **Aturan pemilik (motu) MENANG atas doktrin bawaan skill.** Lihat `LOCAL-NOTES.md` — ini mengikat dan dibaca sebelum skill-skill di hub ini dipakai.
2. **Skill = panduan teks, tidak jalan otomatis.** Tidak ada script, hook, atau perintah yang dieksekusi sendiri; semua langkah dijalankan Muse saat hunting, dan submit tetap butuh persetujuan motu (teks laporan persis + KYC).
3. **HANYA untuk target yang diizinkan.** Program bounty resmi yang motu kerjakan (Ethereum Foundation, Safe, Relay, CoW, Spark, Across) dan target lain yang motu perintahkan eksplisit. Jangan pernah dipakai buat testing tanpa izin.
4. **Vetting 17 Nov 2026: bersih.** 58 file, semuanya `.md` murni (1.001.794 byte), tanpa script/hook. Grep pola mencurigakan bersih — hit "private key" hanya contoh dokumentasi (template JSON GCP dengan placeholder `...`, daftar path LFI, contoh JWT), hit `curl | bash` / `printenv | base64` hanya contoh serangan yang DIDOKUMENTASIKAN sebagai temuan (kasus Codecov, Pwnrequest) dengan host placeholder (`x.<COLLAB>`, attacker.com, evil.com), hit Mimikatz/BloodHound hanya penulisan kasus LAPSUS$ / alat referensi. Host eksternal yang dirujuk semuanya situs resmi/penelitian (github.com, hackerone.com, learn.microsoft.com, attack.mitre.org, crt.sh, portswigger.net, cloud.hacktricks.wiki) atau placeholder. Tidak ada secret hardcode, tidak ada host exfil.
