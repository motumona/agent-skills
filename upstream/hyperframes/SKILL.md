---
name: hyperframes-hub
description: "Hub for the HyperFrames collection (heygen-com/hyperframes, Apache-2.0) - 9 skills for creating and editing video."
---

# HyperFrames — hub lokal (ditulis Muse, 17 Nov 2026)

Koleksi 9 skill resmi HeyGen (heygen-com/hyperframes, Apache-2.0), disalin verbatim ke `skills/`. Dipakai kalau motu minta bikin/edit video. Skill utama dibaca dulu: `skills/hyperframes/SKILL.md`.

## Sub-skill

1. **hyperframes** (`skills/hyperframes/`) — baca dulu sebelum bikin, edit, animasi, atau render video apa pun dengan HyperFrames (HTML dirender jadi video): launch film, explainer, music video, chart, peta, klip vertikal, title card, caption, overlay. Isi kontrak render + alur kerja.
2. **hyperframes-cli** (`skills/hyperframes-cli/`) — CLI HyperFrames: scaffold, cek frame, edit timeline, preview, render, share, riwayat proyek; baca JSON dan pulih dari kegagalan.
3. **hyperframes-registry** (`skills/hyperframes-registry/`) — sekitar 450 blok/komponen siap pakai (transisi, overlay, judul, kinetic type, caption, chart, overlay peta, 3D, gerakan kamera). Cek dulu sebelum bikin visual dari nol.
4. **figma** (`skills/figma/`) — bawa desain Figma ke video HyperFrames (aset, brand token, komponen, frame storyboard).
5. **media-use** (`skills/media-use/`) — cari/buat media buat video: musik, sound effect, gambar, ikon, logo, voiceover, avatar, video generated, transkrip, cutout, color grade. Bisa pakai HeyGen atau alat lokal gratis.
6. **remotion-to-hyperframes** (`skills/remotion-to-hyperframes/`) — bawa kode/footage video yang sudah ada (Remotion dulu, juga Motion Canvas, Lottie, Three.js, p5.js, Manim, After Effects, Blender) ke HyperFrames, verifikasi frame demi frame.
7. **reverse-any-video** (`skills/reverse-any-video/`) — bangun ulang file video apa pun jadi proyek HyperFrames yang bisa diedit, dicek frame demi frame.
8. **slideshow** (`skills/slideshow/`) — bikin slideshow/deck buat presentasi live (reveal, hotspot, presenter mode + speaker notes).
9. **style-sampling** (`skills/style-sampling/`) — bikin episode baru dengan gaya video yang sudah terbukti (Collage Explainer, Finance Explainer, Animated Science Explainer, 3D Brand Explainer, 3D True Crime).

## Catatan lokal (hasil vetting 17 Nov 2026)

- File vendored JANGAN diedit. Catatan ini satu-satunya tambahan lokal.
- CLI dijalankan lewat `skills/hyperframes/scripts/plugin-cli.mjs` (node lokal); instalasi standalone mengambil rilis terbaru dari npm. Bukan program hidup — skill = panduan teks + skrip CLI yang baru jalan kalau dipakai.
- **Telemetri:** `media-use` mengirim pelacakan pemakaian kasar ke PostHog (us.i.posthog.com) — tanpa teks niat, nama file, atau path, menurut header `telemetry.mjs`. Ada opt-out lewat environment variable; jangan aktifkan telemetri tanpa sepengetahuan motu, dan jangan kirim data sensitif lewat skill ini.
- **API key:** fitur HeyGen / ElevenLabs / Gemini di `media-use` baca API key dari environment variable (normal, tidak bocor di file). Motu tidak punya key itu — pakai alat lokal gratis saja kalau motu minta, jangan minta dia beli key.
- Vetting: grep pola mencurigakan di semua script bersih (tidak ada curl|sh, ~/.ssh, private key, secret hardcode); host eksternal yang dipakai wajar buat alat ini (api.heygen.com, Google APIs, Openverse, jsdelivr, freesound, basemap).
