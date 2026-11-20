---
name: query-token-audit
description: Audit keamanan token sebelum trade, mint, atau klaim — deteksi honeypot, rug pull, dan pajak jual/beli lewat API publik Binance Web3, tanpa API key. Dipakai bersama safe-free-mint-gate; BSC chain utama.
---

# Query Token Audit

> Catatan lokal (Muse, 20 Nov 2026): skill ini DITULIS FRESH untuk motu dari pola API publik Binance Web3 — BUKAN salinan skill upstream (repo binance-skills-hub tidak punya file LICENSE, jadi file upstream tidak disalin). Endpoint, parameter, dan arti respons mengikuti dokumentasi publik Binance; aturan pemakaian di bawah ini aturan motu sendiri.

Audit keamanan token SEBELUM trade, mint, klaim, atau jual. Menjawab "apakah token ini aman?" dengan data: risiko honeypot, rug pull, pajak beli/jual, dan fungsi kontrak berbahaya. BUKAN nasihat investasi — hanya bendera risiko.

## Kapan dipakai

1. Sebelum mint/claim gratis apa pun, sesudah alamat kontrak lolos safe-free-mint-gate Aturan 1 (verifikasi dari sumber resmi terbaru).
2. Sebelum swap atau jual token apa pun.
3. Saat motu bertanya "apakah token ini aman?" atau minta cek keamanan token.

## API: Token Security Audit

### Method: POST

```
https://web3.binance.com/bapi/defi/v1/public/wallet-direct/security/token/audit
```

### Parameter

1. `binanceChainId` (wajib): `56` (BSC), `8453` (Base), `1` (Ethereum), `CT_501` (Solana).
2. `contractAddress` (wajib): alamat kontrak token, format checksum.
3. `requestId` (wajib): UUID v4 unik untuk setiap permintaan (buat dengan `python3 -c "import uuid; print(uuid.uuid4())"`).

### Header

```
Content-Type: application/json
Accept-Encoding: identity
User-Agent: binance-web3/1.4 (Skill)
```

Tambahkan juga header `source: agent` seperti contoh dokumentasi publik.

### Contoh (curl)

```bash
UUID=$(python3 -c "import uuid; print(uuid.uuid4())")
curl -s -X POST 'https://web3.binance.com/bapi/defi/v1/public/wallet-direct/security/token/audit' \
  -H 'Content-Type: application/json' \
  -H 'source: agent' \
  -H 'Accept-Encoding: identity' \
  -H 'User-Agent: binance-web3/1.4 (Skill)' \
  --data "{\"binanceChainId\": \"56\", \"contractAddress\": \"<alamat-kontrak>\", \"requestId\": \"$UUID\"}"
```

Tidak butuh API key. Terverifikasi live dari VM ini 20 Nov 2026: API bisa dijangkau (tidak kena geo-block seperti API Binance biasa), CAKE dan WBNB mengembalikan `hasResult: true`, `riskLevel` 1 dan 0.

## Membaca respons

### Kalau tidak ada data

Kalau `hasResult: false` ATAU `isSupported: false`, jawab: "Data audit keamanan tidak tersedia untuk token ini di chain ini." JANGAN tampilkan `riskLevel`, `riskLevelEnum`, atau `riskItems` — datanya tidak bisa diandalkan dalam kondisi itu. Sarankan motu memverifikasi alamat kontrak dan chain, atau coba lagi nanti.

Catatan terverifikasi: token besar seperti USDT BSC mengembalikan `hasResult: false` / `isSupported: false` (dicek live 20 Nov 2026). Itu artinya "tidak ada data audit", BUKAN "aman" dan BUKAN "berbahaya".

### Kalau ada data (`hasResult: true` DAN `isSupported: true`)

Tampilkan hasil lengkap: risk level, pajak, status verifikasi, dan semua risk item.

| riskLevel | riskLevelEnum | Tindakan untuk motu |
|-----------|---------------|---------------------|
| 0-1 | LOW | Lanjut dengan hati-hati — risiko rendah, BUKAN jaminan aman |
| 2-3 | MEDIUM | Hati-hati — tinjau tiap risk item dengan saksama |
| 4 | HIGH | Jangan trade — risiko kritis, kemungkinan rugi tinggi |
| 5 | HIGH | BLOKIR transaksi — jangan lanjut sama sekali |

### Pajak

1. Pajak beli (`extraInfo.buyTax`) dan pajak jual (`extraInfo.sellTax`) dalam persen string.
2. Ambang: >10% = kritis, 5-10% = peringatan, <5% = masih bisa diterima.
3. Pajak tinggi + risk item `TRADE_RISK` yang kena = jangan trade.

### Risk item

1. Kategori: `CONTRACT_RISK` (mekanisme berbahaya di kode kontrak), `TRADE_RISK` (risiko jual/beli), `SCAM_RISK` (indikasi penipuan).
2. Tiap detail punya `title`, `description`, dan `isHit` — `isHit: true` artinya risiko itu TERDETEKSI.
3. `extraInfo.isVerified` = apakah kode kontrak terverifikasi.

## Aturan motu

1. Risk level 4 atau 5 = JANGAN lanjut (jangan mint, jangan klaim, jangan swap, jangan jual-beli). Laporkan alasannya ke motu.
2. LOW bukan berarti aman. Hasil audit adalah snapshot sesaat — tim proyek bisa mengubah kontrak atau mengunci likuiditas sesudahnya. Risiko itu tidak bisa diprediksi dari audit ini.
3. Audit ini TIDAK menggantikan safe-free-mint-gate: verifikasi alamat kontrak dari sumber resmi terbaru, cek kontrol owner, simulasi nilai 0, dan preview baw tetap wajib.
4. Jangan pernah memberi nasihat investasi. Hanya sampaikan bendera risiko + apa artinya.
5. Selalu akhiri dengan disclaimer: `⚠️ Hasil audit ini hanya untuk referensi dan bukan nasihat investasi. Selalu lakukan riset sendiri.`
