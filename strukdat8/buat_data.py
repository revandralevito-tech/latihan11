"""Membuat file Excel data penjualan untuk Kegiatan Praktikum 1.

Nama file diambil dari EXCEL_FILE di .env (bawaan: penjualan.xlsx).

Jalankan sekali:  uv run buat_data.py
"""
import pandas as pd

from config import EXCEL_FILE

data = {
    "Bulan": ["Jan", "Feb", "Mar", "Apr", "Mei", "Jun",
              "Jul", "Agu", "Sep", "Okt", "Nov", "Des"],
    "Produk_A": [120, 135, 150, 160, 180, 200, 210, 220, 230, 210, 190, 170],
    "Produk_B": [80, 90, 110, 130, 150, 160, 180, 190, 195, 200, 180, 160],
    "Produk_C": [60, 70, 75, 85, 95, 120, 130, 140, 150, 145, 130, 125],
}

df = pd.DataFrame(data)
df.to_excel(EXCEL_FILE, index=False)  # index=False: tanpa kolom nomor baris
print(df)
print(f"File {EXCEL_FILE.name} berhasil dibuat.")
