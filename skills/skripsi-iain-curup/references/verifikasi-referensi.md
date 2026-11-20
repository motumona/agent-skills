# Verifikasi Referensi — Cara Memeriksa Sebelum Mengutip

Aturan utama: jangan pernah mengarang referensi, DOI, penulis, tahun,
jurnal, atau halaman. Referensi yang belum terverifikasi ditandai
`[PERLU VERIFIKASI: ...]`.

## 1. Verifikasi metadata (apakah karya ini benar-benar ada?)

Periksa penulis, tahun, judul, wadah publikasi, volume/nomor, halaman
atau nomor artikel, penerbit, dan DOI/URL sebagaimana tercantum pada
publikasi — bukan dari tebakan nama berkas.

- Artikel jurnal internasional / ber-DOI: Crossref REST API, tanpa kunci:
  `curl "https://api.crossref.org/works?query.title=<judul>&query.author=<penulis>&rows=3"`
  Cocokkan judul + penulis + tahun + publikasi. Kecocokan sebagian kata
  belum cukup. Sumber yang tidak ada di Crossref tetap bisa sah —
  periksa lewat sumber asalnya.
- Alternatif metadata: OpenAlex `https://api.openalex.org/works?search=<judul>`,
  dan DOI resolver `https://doi.org/<doi>`.
- Jurnal Indonesia: SINTA (sinta.kemdikbud.go.id) dan Garuda
  (garuda.kemdikbud.go.id) untuk jurnal terakreditasi; periksa juga situs
  jurnal / penerbitnya langsung.
- Buku: periksa lewat penerbit, Google Books, atau katalog perpustakaan.
  Jangan menciptakan DOI untuk buku yang tidak memilikinya.
- Peraturan (UU, KHI, PP): situs resmi — peraturan.go.id, jdih,
  atau situs instansi penerbit. Jangan mengutip peraturan dari ringkasan
  pihak ketiga bila teks resminya tersedia.

## 2. Verifikasi isi (apakah sumber mendukung klaim?)

Baca bagian yang benar-benar digunakan dan simpan halaman / bagian /
tabelnya. Kalau hanya metadata atau abstrak yang tersedia, nyatakan
batas pemeriksaan — jangan menyatakan teks lengkap telah dibaca.
Periksa koreksi atau pencabutan bila tersedia dan relevan.

Tandai tiap klaim: `mendukung` / `terbatas` / `tidak mendukung` /
`belum dibaca`. Klaim sentral, mengejutkan, kuantitatif, atau kontroversial
wajib diperiksa, bukan hanya klaim pinggiran.

## 3. Audit dua arah sitasi ↔ daftar pustaka

Pasangkan setiap footnote dalam teks dengan entri daftar pustaka, lalu
periksa entri yang tidak punya pasangan di teks. Cocokkan berdasarkan
identitas karya, bukan sekadar ejaan penulis.

| Lokasi/klaim | Sitasi/entri | Metadata | Isi pendukung | Format/pasangan | Tindakan |
| --- | --- | --- | --- | --- | --- |
| [lokasi] | [identitas] | [terverifikasi/sebagian/belum] | [mendukung/terbatas/tidak mendukung/belum dibaca] | [temuan] | [perbaikan konkret] |

## 4. Format Chicago 17th Full Note (gaya pedoman IAIN Curup)

- Footnote memakai catatan lengkap pada kutipan pertama (Full Note),
  bukan author-date. Nomor footnote berurutan mulai dari 1.
- Kutipan langsung mempertahankan teks asli + penunjuk lokasi (halaman).
- Parafrasa mengubah susunan penyampaian dengan pemahaman benar, tetap
  dengan atribusi. Jangan mengganti kata secara mekanis untuk
  menyembunyikan penyalinan.
- Daftar pustaka disusun sesuai Chicago 17th; tiap entri harus punya
  pasangan footnote di teks, dan sebaliknya.
- Kalau ada keraguan format untuk satu jenis sumber (mis. peraturan,
  kitab fikih klasik, website), baca bagian gaya pengutipan di Bab IV
  Teknik Penulisan pedoman sebelum memutuskan — jangan menebak.

## 5. Alat pengelola referensi

Zotero / Mendeley boleh dipakai untuk mengelola referensi dan membuat
daftar pustaka (format Chicago). Periksa hasil impornya sebelum menganggap
sitasi benar — aplikasi bisa membawa metadata yang salah. Jangan mengklaim
pustaka pengguna sudah tersinkronisasi bila hanya memberikan langkah
penggunaan atau berkas ekspor.

## 6. Yang tidak boleh dilakukan

- Mengarang referensi, DOI, atau halaman agar daftar pustaka terlihat penuh.
- Menyatakan pencarian atau verifikasi sudah dilakukan padahal belum.
- Mengutip AI sebagai penulis jurnal. Kalau AI dipakai untuk menemukan
  sumber, yang dikutip adalah sumber aslinya setelah dibaca dan diverifikasi.
- Menjanjikan lolos detektor AI atau pemeriksaan plagiarisme.
