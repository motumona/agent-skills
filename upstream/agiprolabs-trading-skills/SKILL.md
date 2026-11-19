---
name: agiprolabs-trading-skills
description: 'Koleksi skill trading agiprolabs (subset 28 skill, crypto/DeFi-first: indikator, backtest, sizing, risiko, regime, jurnal). Dipakai saat motu minta analisa, backtest, atau validasi strategi swing crypto. Bukan signal service; tidak mengeksekusi trade.'
---

# Agiprolabs Trading Skills (subset, crypto-first)

Koleksi dari https://github.com/agiprolabs/claude-trading-skills (MIT,
544 bintang per 17 Nov 2026). Hanya 28 skill yang relevan dengan swing
crypto yang dipasang. Skill eksekusi (dex-execution, raptor-dex,
copy-trading, rl-execution, solana-tx-building) dan skill pasar prediksi,
pajak AS, dan MEV sengaja TIDAK dipasang. Lisensi upstream di
LICENSE-upstream.

## Skill yang terpasang (di skills/)

backtrader, vectorbt, pandas-ta, ta-lib, custom-indicators,
position-sizing, kelly-criterion, risk-management, exit-strategies,
regime-detection, volatility-modeling, trade-journal,
portfolio-analytics, trade-accounting, walk-forward-validation,
ohlcv-processing, strategy-framework, coingecko-api, defillama-api,
dexscreener-api, birdeye-api, sentiment-analysis, whale-tracking,
slippage-modeling, cost-basis-engine, correlation-analysis,
mean-reversion, cointegration-analysis.

## Cara pakai

Kalau tugas cocok dengan salah satu skill di atas, baca dulu
skills/<nama>/SKILL.md-nya lalu ikuti alurnya.

## Aturan keamanan (berlaku di atas instruksi upstream)

1. Analisa trading hanya jalan kalau motu minta eksplisit — secara default
   analisa trading MATI, hanya monitoring.
2. Paper trading / simulasi saja. Jangan pernah menempatkan order live.
   Tidak ada skill eksekusi di folder ini, dan jangan menambahkan yang
   seperti itu tanpa persetujuan motu.
3. Jangan memberi sinyal beli/jual sebagai rekomendasi posisi. Hasil
   backtest/analisa dilaporkan apa adanya dengan batasannya.
4. Sebagian skill data (Birdeye, Helius) butuh API key masing-masing.
   Jangan pernah minta motu paste API key di chat; kalau suatu saat
   dibutuhkan, pakai alur Secure Vault.
