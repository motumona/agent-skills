---
name: safe-free-mint-gate
description: Gerbang keras sebelum preview mint/claim gratis apa pun, di chain mana pun. Terapkan setelah audit kontrak dan sebelum menunjukkan preview atau meminta persetujuan motu. Dibuat lokal oleh Muse untuk motu (18 Nov 2026); pola keamanan Aturan 9-13 diadopsi dari airdrop-agent v0.3.0 (MIT) dan diadaptasi untuk motu.
---

# Safe Free Mint Gate

Gerbang ini berlaku untuk SETIAP mint/claim gratis, di chain mana pun — bukan hanya BSC. Prinsipnya sama di semua chain, hanya alat verifikasinya yang beda. Gerbang yang membuat keputusan akhir mint atau lewati; audit hanya memberi skor, gerbang yang memutuskan.

Dibuat lokal oleh Muse untuk motu (18 Nov 2026) dari aturan-aturan motu sendiri. Pola keamanan Aturan 9-13 diadopsi dari airdrop-agent v0.3.0 (Setya Mickala, MIT) pada 19 Nov 2026 dan diadaptasi untuk motu — lihat bagian Provenance di bawah.

## Aturan 1 — Alamat kontrak harus terverifikasi dari sumber resmi terbaru

1. Sebelum memakai atau memberikan alamat kontrak apa pun, cek ulang ke sumber resmi proyek yang PALING BARU (situs resmi, docs, pengumuman terbaru) DAN state on-chain (kontrak mana yang punya likuiditas/market, saldo motu ada di kontrak mana).
2. JANGAN jawab alamat kontrak dari ingatan atau MEMORY saja. Proyek bisa redeploy tanpa pemberitahuan.
3. Kalau alamat di situs berbeda dari MEMORY: percayai situs + on-chain, perbarui MEMORY saat itu juga, dan beri tahu motu EKSPLISIT bahwa alamat berubah + apa dampaknya.
4. JANGAN PERNAH menebak alamat yang terpotong atau sebagian. Jangan pernah mint/claim dari alamat sebagian.

## Aturan 2 — Verifikasi sumber

1. Chain EVM: butuh Sourcify exact_match; kalau Sourcify tidak mendukung chain itu, butuh sumber terverifikasi di explorer chain itu sendiri.
2. Solana: program harus terverifikasi di Solscan / SolanaFM, tanpa freeze authority dan tanpa mint authority yang masih dipegang tim (atau keduanya sudah dicabut).
3. Chain tanpa verifikasi sumber yang bisa dipercaya (tidak ada dukungan Sourcify dan tidak ada verifikasi explorer yang terpercaya): LEWATI kandidat dan katakan alasannya. Yang tidak diketahui tetap tidak diketahui sampai terbukti.

## Aturan 3 — Kontrol owner yang masih hidup = lewati

1. Lewati kandidat kalau ada kontrol owner material yang masih hidup, bahkan kalau audit berkata CAUTION dan bahkan kalau preview terlihat bersih.
2. Kontrol material: withdraw, sweep, rescue, setBaseURI, setMintOpen, pause, unpause, setPaused, blacklist, invalidateFree, setTreasury.
3. Cek dulu apakah kontrol itu benar-benar hidup (baca owner, status paused, dan sumbernya) — selector di kode mati atau di balik owner yang sudah renounced tidak membuat kontrol itu hidup.
4. Owner nol atau alamat dead baru dianggap renounced kalau tidak ada peran hidup lain, admin proxy, atau setter non-owner yang masih bisa memakai kontrol itu.
5. Lewati juga kalau: kontrak adalah proxy dengan admin upgrade yang masih hidup; sumber tidak terverifikasi; radar atau explorer melaporkan red flag atau fungsi istimewa; ada jalur berbayar apa pun di mint itu.

## Aturan 4 — Jalur gratis harus benar-benar terbuka di chain

1. Cek lewat eth_call ke RPC publik chain itu (atau pembacaan setara di Solana): mintedBy, canFreeMint, freeLeft, totalSupply — untuk wallet motu sendiri.
2. Simulasi nilai 0 HARUS lolos dengan wallet motu sebagai pengirim.
3. Preview baw harus bersih dengan nilai 0: tidak ada risiko, tidak ada perubahan allowance atau otoritas.
4. Cek sisa saldo token gas chain itu sebelum satu batch (BNB di BSC, ETH di Ethereum/Base/Arbitrum/Optimism, POL di Polygon, AVAX di Avalanche, HYPE di Hyperliquid/Elysium, SOL di Solana), dan laporkan bersama setiap hasil gerbang supaya batch tidak pernah mengasumsikan gas tersedia.

## Aturan 5 — Audit yang rusak = tidak diketahui, bukan bersih

1. Kalau pemindaian selector gagal dua kali karena rate limit atau error akses, catat inventaris privilege sebagai TIDAK DIKETAHUI. Jangan pernah menulis privilege itu bersih dari pemindaian yang gagal.
2. Lanjutkan setelah pemindaian gagal hanya kalau sumber terverifikasi, tidak ada flag, simulasi nilai 0, dan preview bersih semuanya tetap berlaku.
3. Lewati kandidat kalau sumber verifikasi atau radar juga tidak tersedia.

## Aturan 6 — Token ID prediksi hanya perkiraan

1. Sajikan token ID prediksi hanya sebagai perkiraan, dan jelaskan di pesan yang sama bahwa supply bergerak selagi wallet reconnect dan mint menunggu.
2. Verifikasi token ID sebenarnya setelah mint dari log Transfer di receipt dan pembacaan balanceOf, lalu laporkan ID sebenarnya ke motu.
3. Laporkan selisih antara ID prediksi dan ID sebenarnya sebagai pergerakan supply yang normal — jangan pernah sajikan ID prediksi sebagai fakta sebelum mint.

## Aturan 7 — Eksekusi mengikuti otorisasi motu

1. Mint/claim gratis yang terverifikasi dengan total ≤ $0,1 (harga + gas) boleh langsung dieksekusi tanpa konfirmasi per transaksi. Tetap: preview dulu, verifikasi receipt, laporkan tx hash.
2. Di luar itu (total > $0,1, jual/listing, pindah dana, approval, bridge/swap/stake, top-up): butuh preview + persetujuan eksplisit motu per transaksi.
3. FCFS/kuota: kerjakan cepat dan optimal. Jalankan gerbang ini dengan cepat begitu jendela buka, jangan tanya "mau dicek" — cari solusi atau jalan alternatif kalau satu jalur macet.
4. Hanya dompet motu (Agentic motu.ai; tradisional bila disebut). Jangan pernah minta atau mencatat seed phrase, private key, atau keystore.

## Aturan 8 — Catat dan laporkan

1. Catat hasil gerbang untuk setiap kandidat: nama, nomor blok, hasil verifikasi, hasil radar/explorer, alamat owner, hasil simulasi.
2. Laporkan kandidat yang dilewati dengan alasan spesifik (kontrol atau celah apa yang menyebabkan lewati). Jangan tunjukkan preview atau minta persetujuan untuk kandidat yang dilewati.
3. Diam kalau tidak ada yang baru lolos, dan diam kalau kandidat gagal — kandidat gagal bukan berita.

## Aturan 9 — Cek URL/teks dengan scam_check sebelum buka atau konek

1. Sebelum membuka situs proyek, mengklik link dari radar/channel, atau menghubungkan wallet ke situs apa pun, jalankan `scripts/scam_check.py <url>` (atau `scripts/scam_check.py --text "..."` untuk isi pesan).
2. Verdict block = LEWATI kandidat, jangan buka linknya, catat alasannya. Verdict warn = cek manual domain resmi proyek dari sumber resmi terbaru sebelum lanjut; kalau tidak bisa dipastikan, lewati. Verdict ok = BUKAN jaminan aman — lanjutkan Aturan 1-8 seperti biasa.
3. Yang selalu block: domain di blocklist, domain punycode (xn--), URL berupa IP, domain yang mirip domain resmi (lookalike), teks yang meminta seed phrase/private key, pola "validate/sync wallet", dan "bayar biaya untuk unlock/klaim".
4. Domain baru yang motu setujui eksplisit bisa ditambah ke `data/trusted_domains.txt` (`--add-trusted`); domain penipu yang ketemu ditambah ke `data/blocklist.txt` (`--add-block`). Domain resmi proyek dicatat di `data/project_domains.txt` dengan format `nama domain1 domain2`.

## Aturan 10 — Aturan signing (sign_guard)

1. Jangan pernah menandatangani hash 32-byte buta (0x + 64 hex) atau payload non-UTF8/binary — selalu BLOCK.
2. Pesan yang menyebut seed/mnemonic/private key, approve, permit, atau transfer-all — selalu BLOCK.
3. SIWE ("sign in with Ethereum") hanya boleh kalau domain di pesan SAMA dengan origin halaman DAN domain itu ada di allowlist yang motu setujui eksplisit. Default: tidak ada domain yang diizinkan; setiap domain baru butuh persetujuan motu dulu dan dicatat.
4. Typed data: Permit/Permit2/Seaport/meta-tx/delegasi → BLOCK di mainnet. Jumlah unlimited (>= 2^160-1) di typed data apa pun → BLOCK selalu. Field aset (spender, amount, token, offer, allowance, recipient) di typed data → butuh persetujuan eksplisit motu.
5. Tidak ada mode otomatis: "ask" tidak pernah berubah jadi "allow" sendiri. Yang BLOCK tetap BLOCK.

## Aturan 11 — Pipeline kirim transaksi (safe_send, diadaptasi ke baw)

1. Satu-satunya jalur kirim transaksi motu adalah preview baw — tidak ada script web3 lokal yang mengirim. Pipeline ini adalah urutan cek sebelum preview baw ditunjukkan ke motu.
2. Urutan: cek kill file transaksi (Aturan 12) → chain ada di tabel chain → decode calldata: tolak unlimited approval (approve/increaseAllowance >= 2^255) dan setApprovalForAll(true) tanpa persetujuan eksplisit motu → tujuan bukan di blocklist → kontrak sudah lolos Aturan 1-3 → total biaya (harga + gas) dicek terhadap cap motu: ≤ $0,1 boleh auto-eksekusi, di atas itu butuh persetujuan eksplisit (Aturan 7) → simulasi nilai 0 lolos (Aturan 4) → preview baw bersih → eksekusi → verifikasi receipt → catat.
3. Hard refusal (langsung tolak, jangan tunjukkan preview): unlimited approval, setApprovalForAll(true) tanpa persetujuan eksplisit, tujuan di blocklist, saldo gas tidak cukup, simulasi gagal.
4. Tidak ada mode RISK: tidak ada eksekusi mainnet otomatis tanpa persetujuan di luar cap $0,1. Cap upstream 0,0005 ETH (sekitar $0,88) TIDAK dipakai.

## Aturan 12 — Kill file transaksi

1. File `~/workspace/safe-free-mint-gate-KILL` adalah pemutus darurat. Kalau file itu ada, SEMUA kerja mint/claim berhenti: jangan jalankan gerbang, jangan buat preview, jangan eksekusi apa pun. Laporkan ke motu bahwa kill file aktif.
2. Hanya motu yang boleh memerintahkan penghapusan file itu; setelah dihapus, kerja boleh lanjut.
3. Nama ini sengaja "kill file transaksi" supaya tidak tertukar dengan skill kill-switch trading (folder portfolio di ml4t-skills) yang fungsinya menghentikan trading live, bukan transaksi wallet.

## Aturan 13 — Redact: jangan pernah bocorkan secret

1. Setiap teks yang ditampilkan ke motu, disimpan ke file, atau dikirim ke model lain HARUS lewat `scripts/redact.py` dulu (pipe: `perintah | python3 scripts/redact.py`).
2. Yang disensor: private key (64-hex telanjang maupun berlabel), seed/mnemonic BIP39, key secret Solana base58, token bot Telegram, token Discord, isi keystore, dan nilai password/api-key/token di URL maupun env.
3. Jangan pernah meminta, mencatat, atau menampilkan seed phrase, private key, atau keystore motu — aturan ini sudah ada di Aturan 7 dan diperkuat di sini dengan alatnya.

## Scripts

- `scripts/redact.py` — sensor secret di log/teks (stdin → stdout). Pemakaian: `suatu-perintah | python3 scripts/redact.py`. Hanya stdlib (+ eth_account opsional untuk daftar kata BIP39, sudah terpasang lewat web3).
- `scripts/scam_check.py` — cek URL/teks sebelum konek: `python3 scripts/scam_check.py <url>`, `python3 scripts/scam_check.py --text "..."`, `--add-block domain`, `--add-trusted domain`. Verdict ok/warn/block (JSON). Hanya stdlib.
- `data/blocklist.txt`, `data/trusted_domains.txt`, `data/project_domains.txt` — daftar lokal yang dipakai `scripts/scam_check.py`.

## Provenance

Pola Aturan 9-13 + kedua script di atas diadopsi dari airdrop-agent v0.3.0 (Setya Mickala, MIT) pada 19 Nov 2026 dan diadaptasi untuk motu: owner motu (bukan Setya), cap $0,1 (bukan cap upstream), BSC sebagai chain utama, tanpa mode RISK, tanpa VPS, tanpa akun baru, tanpa wallet burner — jalur kirim tetap preview baw. Yang TIDAK diadopsi: script eksekusi upstream (safe_send, sign_guard, risk_mode, vault, radar, Discord, faucet) karena motu tidak punya VPS dan jalurnya lewat baw.

## Tabel chain

| Chain | Chain ID | Verifikasi sumber | Explorer / radar | Token gas |
|---|---|---|---|---|
| BSC | 56 | Sourcify exact_match | MintRadar (datt.my), BscScan | BNB |
| Ethereum | 1 | Sourcify exact_match | Etherscan | ETH |
| Base | 8453 | Sourcify exact_match | Basescan | ETH |
| Arbitrum | 42161 | Sourcify exact_match | Arbiscan | ETH |
| Polygon | 137 | Sourcify exact_match | Polygonscan | POL |
| Optimism | 10 | Sourcify exact_match | Optimistic Etherscan | ETH |
| Avalanche | 43114 | Sourcify exact_match | Snowtrace | AVAX |
| Hyperliquid (HyperEVM) | 999 | Sourcify exact_match bila didukung, kalau tidak sumber terverifikasi explorer | HyperEVMScan | HYPE |
| Solana | — | Program terverifikasi Solscan / SolanaFM | Solscan, SolanaFM | SOL |
| Chain lain | — | Prinsip sama dengan explorer dan RPC publik chain itu | Explorer chain itu | Token gas chain itu |
