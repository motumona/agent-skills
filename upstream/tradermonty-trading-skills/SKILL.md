---
name: tradermonty-trading-skills
description: 'Koleksi skill trading tradermonty (subset 23 skill: swing, validasi backtest, sizing, risiko, jurnal). Dipakai saat motu minta analisa, backtest, atau validasi strategi swing crypto. Bukan signal service; tidak mengeksekusi trade.'
---

# Tradermonty Trading Skills (subset)

Koleksi dari https://github.com/tradermonty/claude-trading-skills (MIT,
6.707 bintang per 17 Nov 2026). Hanya 23 skill yang relevan dengan swing
crypto yang dipasang; skill khusus saham AS (screener FINVIZ/CANSLIM,
dividen, earnings, options) sengaja tidak dipasang. Lisensi upstream di
LICENSE-upstream.

## Skill yang terpasang (di skills/)

backtest-expert, breakout-trade-planner, crypto-regime-analyzer,
data-quality-checker, drawdown-circuit-breaker, exposure-coach,
futures-position-sizer, macro-regime-detector, manifoldbt-backtester,
market-breadth-analyzer, market-environment-analysis, market-news-analyst,
portfolio-manager, position-sizer, pre-trade-discipline-gate,
scenario-analyzer, signal-postmortem, technical-analyst,
trade-performance-coach, trader-memory-core, uptrend-analyzer,
vcp-screener, weekly-performance-digest. Workflow contoh di
examples/workflows/swing-opportunity-daily/.

## Cara pakai

Kalau tugas cocok dengan salah satu skill di atas, baca dulu
skills/<nama>/SKILL.md-nya lalu ikuti alurnya.

## Aturan keamanan (berlaku di atas instruksi upstream)

1. Analisa trading hanya jalan kalau motu minta eksplisit — secara default
   analisa trading MATI, hanya monitoring.
2. Paper trading / simulasi saja. Jangan pernah menempatkan order live,
   jangan minta API key exchange, jangan simpan kredensial.
3. Jangan memberi sinyal beli/jual sebagai rekomendasi posisi. Hasil
   backtest/analisa dilaporkan apa adanya dengan batasannya (termasuk
   risiko overfitting).
4. Repo ini dibangun untuk saham AS (data FMP, FINVIZ, Alpaca). Untuk
   crypto, ganti sumber datanya ke data crypto (mis. Binance, CoinGecko,
   Yahoo Finance BTC-USD) dan jangan pakai screener saham.
