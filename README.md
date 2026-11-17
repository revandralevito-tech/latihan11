# Praktikum Struktur Data – Visualisasi Data

Proyek ini berisi dua kegiatan praktikum dari modul Pertemuan 11 (Bab 8, Visualisasi Data). Keduanya memakai **Matplotlib** untuk membuat grafik dan **Streamlit** untuk menampilkannya di web.

| File | Isi |
|---|---|
| `praktikum1.py` | Kegiatan Praktikum 1: visualisasi data penjualan dari file Excel (line, bar, scatter, histogram dalam satu kanvas 2×2) |
| `praktikum2.py` | Kegiatan Praktikum 2: visualisasi data Pokémon dari PokeAPI (metrik rata-rata, bar, barh, scatter, histogram) |
| `config.py` | Membaca `.env` dan menyediakan pengaturan untuk semua script |
| `buat_data.py` | Membuat file `penjualan.xlsx` |
| `penjualan.xlsx` | Data penjualan Produk A, B, C selama 12 bulan |
| `.env` | Pengaturan aplikasi: judul, URL PokeAPI, batas slider, timeout, nama file Excel |
| `.env.example` | Contoh isi `.env` |

## Cara menjalankan

Proyek ini dikelola dengan [uv](https://docs.astral.sh/uv/).

```bash
uv sync                               # pasang semua dependensi
uv run streamlit run praktikum1.py    # Praktikum 1
uv run streamlit run praktikum2.py    # Praktikum 2
```

Di Praktikum 1, unggah file Excel lewat tombol upload. Jika belum ada yang diunggah, aplikasi otomatis memakai file `EXCEL_FILE` dari `.env` (bawaan: `penjualan.xlsx`). Praktikum 2 butuh koneksi internet karena datanya diambil dari PokeAPI.

## Konfigurasi (.env)

Pengaturan aplikasi disimpan di file `.env`. File `config.py` membacanya dengan `python-dotenv`, lalu `praktikum1.py`, `praktikum2.py`, dan `buat_data.py` mengambil nilainya dari `config.py`. Setelah mengubah `.env`, jalankan ulang aplikasinya. Ubah nilainya di sana tanpa menyentuh kode, misalnya `POKEMON_MAX=50` agar slider bisa sampai 50 Pokémon. Jika `.env` tidak ada, aplikasi memakai nilai bawaan di kode.

## Dependensi

pandas, streamlit, openpyxl, matplotlib, requests, python-dotenv
