---
name: ml4t-skills
description: 61 skill Markdown dari buku Machine Learning for Algorithmic Trading (Stefan Jansen) — validasi anti-overfit, walk-forward CV, deflated Sharpe, purging dan embargo, biaya transaksi, triple-barrier labelling, position sizing, kill-switch. Dipakai saat memvalidasi backtest atau merancang strategi sistematis. Tanpa script, tanpa jaringan.
---

# ML4T Skills (Machine Learning for Algorithmic Trading)

61 skill dari https://github.com/ml4t/skills (Apache-2.0, pendamping buku
Machine Learning for Algorithmic Trading edisi ke-3). Isinya murni file
Markdown (SKILL.md + frontmatter) — tanpa script, tanpa hook, tanpa MCP,
tanpa panggilan jaringan. Pemetaan skill ke bab buku ada di
SKILL_CHAPTER_MAP.md. Lisensi upstream di LICENSE-upstream.

## Kelompok skill (di folder topik)

advanced-ai, backtest, concepts, data, features, infrastructure,
portfolio, production, validation, workflows.

## Cara pakai

Kalau tugas cocok dengan salah satu skill, baca SKILL.md di folder
topiknya lalu ikuti alurnya.

## Aturan keamanan (berlaku di atas instruksi upstream)

1. Analisa trading hanya jalan kalau motu minta eksplisit — secara default
   analisa trading MATI, hanya monitoring.
2. Skill ini penjaga disiplin, bukan pemberi sinyal: jangan pakai untuk
   merekomendasikan posisi beli/jual. Laporkan hasil validasi apa adanya,
   termasuk risiko overfitting dan keterbatasan data.
3. Butuh kerja sendiri (menulis kode) — bukan plug-and-play.
