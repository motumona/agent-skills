---
name: airdrop-research
description: Mencari dan memeriksa kandidat airdrop / free mint di semua chain untuk wallet motu, lalu menyaringnya lewat safe-free-mint-gate sebelum dilaporkan. Riset publik saja — tanpa login ke mana pun. Dibuat lokal oleh Muse untuk motu (18 Nov 2026) dari alur kerja motu sendiri — bukan salinan repo mana pun.
---

# Airdrop Research

Cari kandidat airdrop dan free mint di semua chain, periksa satu per satu, dan laporkan hanya yang lolos gerbang penuh. Skill ini hanya mencari dan memeriksa — tidak pernah mint atau claim sendiri.

## Cari kandidat — di chain mana pun

1. Cari di semua chain tempat free mint muncul: BSC, Ethereum, Base, Arbitrum, Polygon, Optimism, Avalanche, Hyperliquid (HyperEVM), Solana, dan chain lain.
2. Mulai dari radar dan sumber komunitas, bukan dari tautan acak di balasan atau DM:
   - MintRadar (https://datt.my/) untuk kontrak free mint terbaru di BSC.
   - Alphapedia (https://boltbook.fun/alphapedia) untuk listing proyek baru.
   - Alpha Board (https://boltbook.fun/b/alpha?topic=airdrop) untuk drop yang dibagikan komunitas.
   - Chain lain: explorer chain itu (Etherscan, Basescan, Arbiscan, Polygonscan, Snowtrace, HyperEVMScan) dan sumber komunitasnya. Solana: Solscan dan SolanaFM.
3. Riset X HANYA dari postingan publik — baca tanpa login. JANGAN login ke X, JANGAN paksa login ulang, JANGAN posting/like/follow/repost lewat browser. Motu yang posting sendiri, jarang saja. Cari kata testnet, event, instant, FCFS, dan whitelist, lalu verifikasi setiap kandidat sebelum dilaporkan.
4. Sumber testnet dicek terpisah: docs atau pengumuman resmi proyek untuk program testnet, halaman faucet testnet, dan explorer testnet untuk alamat kontraknya.
5. Anggap kandidat sebagai baru hanya kalau alamat kontrak lengkapnya belum ada di daftar sudah-mint, dilewati, atau dilaporkan — dan disajikan gratis untuk wallet Binance Agent ID.
6. Lewati kandidat yang satu-satunya sumber adalah balasan, DM, atau postingan sosial yang belum terverifikasi tanpa tautan ke pengumuman resmi atau kontrak yang bisa diverifikasi.

## Urutkan berdasarkan jenis

1. Testnet: tugas berjalan di testnet, token hadiah tidak punya nilai mainnet, satu-satunya biaya adalah token faucet testnet plus waktu.
2. Instant: claim sudah live sekarang, hadiah langsung masuk wallet, jendelanya pendek.
3. Event: drop terikat tanggal (peluncuran, hari libur, milestone) dengan waktu mulai dan selesai yang dinyatakan.
4. FCFS: siapa cepat dia dapat, slot atau wallet terbatas, tutup kalau sudah penuh. Catat berapa slot tersisa.
5. Whitelist: pendaftaran whitelist (form, tugas, atau on-chain) dengan deadline dan syarat yang jelas.
6. Catat jenis, chain, deadline, dan sumber untuk setiap kandidat — instant drop dan event drop butuh urgensi yang berbeda.

## Periksa setiap kandidat lewat gerbang

1. Terapkan `safe-free-mint-gate` sebelum menunjukkan preview atau meminta persetujuan motu.
2. Butuh sumber terverifikasi di chain kandidat itu sendiri: Sourcify exact_match untuk chain EVM (atau sumber terverifikasi explorer kalau Sourcify tidak mendukung chain itu), dan verifikasi program di Solscan / SolanaFM untuk Solana.
3. Butuh radar atau explorer melaporkan tidak ada flag dan tidak ada fungsi istimewa.
4. Butuh jalur gratis benar-benar terbuka di chain untuk wallet motu: cek mintedBy, canFreeMint, freeLeft, dan totalSupply lewat eth_call ke RPC publik chain itu (atau pembacaan setara untuk Solana).
5. Butuh simulasi nilai 0 lolos, dengan wallet motu sebagai pengirim.
6. Butuh preview baw yang bersih dengan nilai 0, tanpa risiko, tanpa perubahan allowance atau otoritas.
7. Lewati apa pun yang sumbernya tidak terverifikasi, ada red flag atau backdoor, proxy yang bisa di-upgrade, kontrol owner material, atau jalur berbayar.

## Aturan testnet

1. Jangan pernah menghabiskan dana mainnet untuk program testnet, dan jangan pernah bridge aset asli ke testnet untuk airdrop.
2. Token testnet hanya dari faucet resmi, dan anggap saldo testnet tidak berharga.
3. Verifikasi alamat kontrak testnet di explorer testnet, dan pastikan chain ID cocok dengan pengumuman program.
4. Program testnet yang meminta deposit mainnet, koneksi wallet dengan persetujuan belanja, atau seed phrase adalah penipuan — berhenti.
5. Catat partisipasi testnet terpisah dari claim mainnet, karena aktivitas testnet untuk kelayakan dan belajar, bukan untuk nilai.

## Aturan instant dan event

1. Verifikasi event dari akun resmi proyek atau halaman pengumuman resmi sebelum membagikannya — postingan event palsu adalah penipuan airdrop yang paling umum.
2. Cek deadline di chain kalau kontrak menyediakan mint end atau sale end, dan laporkan deadline dalam zona waktu motu (WIB).
3. Peringatkan motu kalau jalur gratis hampir habis, dan verifikasi ulang jumlah gratis sebelum eksekusi apa pun, karena jalur yang sudah penuh akan revert.
4. Jangan pernah membagikan tautan claim yang belum dibuka dan dicek, dan jangan pernah meminta motu menghubungkan wallet di halaman yang belum terverifikasi.

## Laporkan, jangan pernah auto-claim

1. Laporkan hanya kandidat yang lolos gerbang penuh, dengan nama koleksi, chain, alamat kontrak, apa itu, ringkasan audit, deadline, dan perkiraan token atau NFT id.
2. Minta persetujuan eksplisit motu dengan menyebut nama sebelum mint atau claim apa pun, dan jangan pernah mint/claim atas jawaban "ya" yang kosong kalau ada dua penawaran atau lebih yang terbuka.
3. Catat setiap kandidat di daftar dilaporkan atau dilewati beserta alasannya, nomor blok, hasil verifikasi, hasil radar atau explorer, alamat owner, dan hasil simulasi.
4. Diam kalau tidak ada yang baru lolos, dan diam kalau kandidat gagal — kandidat gagal bukan berita.
5. Jangan pernah meminta approval atau transfer NFT atas nama motu, dan jangan pernah membiarkan wallet melewati batas mint yang motu tetapkan.
