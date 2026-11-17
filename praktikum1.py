import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

from config import APP1_TITLE, EXCEL_FILE

KOLOM_WAJIB = ["Bulan", "Produk_A", "Produk_B", "Produk_C"]

st.title(APP1_TITLE)

uploaded_file = st.file_uploader("Unggah file Excel (.xlsx)", type=["xlsx"])

if uploaded_file is not None:
    sumber = uploaded_file
    st.caption(f"Memakai file yang diunggah: **{uploaded_file.name}**")
elif EXCEL_FILE.exists():
    sumber = EXCEL_FILE
    st.caption(f"Belum ada file yang diunggah. Memakai file bawaan dari .env: **{EXCEL_FILE.name}**")
else:
    st.info(
        f"Silakan unggah file Excel terlebih dahulu. File bawaan `{EXCEL_FILE.name}` "
        "tidak ditemukan; buat dengan `uv run buat_data.py`."
    )
    st.stop()

df = pd.read_excel(sumber)

kurang = [k for k in KOLOM_WAJIB if k not in df.columns]
if kurang:
    st.error(f"Kolom berikut tidak ada di file Excel: {', '.join(kurang)}")
    st.stop()

st.subheader("Data Penjualan")
st.dataframe(df)

fig, axes = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle("Visualisasi Data Penjualan Produk", fontsize=14, fontweight="bold")

axes[0, 0].plot(df["Bulan"], df["Produk_A"], marker="o", label="Produk A")
axes[0, 0].plot(df["Bulan"], df["Produk_B"], marker="s", label="Produk B")
axes[0, 0].plot(df["Bulan"], df["Produk_C"], marker="^", label="Produk C")
axes[0, 0].set_title("Tren Penjualan Bulanan")
axes[0, 0].legend()
axes[0, 0].grid(True, linestyle="--", alpha=0.6)

axes[0, 1].bar(df["Bulan"], df["Produk_A"], color="skyblue", edgecolor="black")
axes[0, 1].set_title("Penjualan Produk A")
axes[0, 1].grid(axis="y", linestyle="--", alpha=0.6)

axes[1, 0].scatter(df["Produk_A"], df["Produk_B"],
                   color="orange", s=80, alpha=0.7, edgecolor="black")
axes[1, 0].set_title("Korelasi Produk A dan B")
axes[1, 0].set_xlabel("Produk A")
axes[1, 0].set_ylabel("Produk B")
axes[1, 0].grid(True, linestyle="--", alpha=0.5)

axes[1, 1].hist(df["Produk_C"], bins=6,
                color="lightgreen", edgecolor="black", rwidth=0.9)
axes[1, 1].set_title("Distribusi Penjualan Produk C")
axes[1, 1].grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout(rect=[0, 0, 1, 0.96])

st.pyplot(fig)
plt.close(fig)  
