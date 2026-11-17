import matplotlib.pyplot as plt
import pandas as pd
import requests
import streamlit as st

from config import (APP2_TITLE, POKEAPI_URL, POKEMON_DEFAULT, POKEMON_MAX,
                    POKEMON_MIN, REQUEST_TIMEOUT)



@st.cache_data(show_spinner=False)
def ambil_data_pokemon(limit: int) -> pd.DataFrame:
    with requests.Session() as session:
        response = session.get(POKEAPI_URL, params={"limit": limit}, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()

        pokemon_list = []
        for item in response.json()["results"]:
            detail_resp = session.get(item["url"], timeout=REQUEST_TIMEOUT)
            detail_resp.raise_for_status()
            detail = detail_resp.json()
            pokemon_list.append({
                "name": detail["name"].capitalize(),
                "height": detail["height"],
                "weight": detail["weight"],
                "abilities": len(detail["abilities"]),  # jumlah kemampuan
            })

    return pd.DataFrame(pokemon_list)


st.title(APP2_TITLE)

limit = st.slider("Pilih jumlah Pokémon yang ingin ditampilkan:",
                  POKEMON_MIN, POKEMON_MAX, POKEMON_DEFAULT)

try:
    with st.spinner("Mengambil data dari PokeAPI..."):
        df = ambil_data_pokemon(limit)
except requests.RequestException as e:
    st.error(f"Gagal mengambil data dari PokeAPI: {e}")
    st.stop()

st.subheader("Data Pokémon")
st.dataframe(df)

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Rata-rata Tinggi", f"{df['height'].mean():.2f}")
with col2:
    st.metric("Rata-rata Berat", f"{df['weight'].mean():.2f}")
with col3:
    st.metric("Rata-rata Ability", f"{df['abilities'].mean():.2f}")

st.subheader("📊 Visualisasi Data Pokémon")

colA, colB = st.columns(2)

with colA:
    st.write("### Grafik Tinggi Pokémon")
    fig1, ax1 = plt.subplots()
    ax1.bar(df["name"], df["height"], color="skyblue")
    ax1.set_xlabel("Nama Pokémon")
    ax1.set_ylabel("Tinggi")
    ax1.tick_params(axis="x", rotation=45)  
    st.pyplot(fig1)
    plt.close(fig1)

with colB:
    st.write("### Grafik Berat Pokémon")
    fig2, ax2 = plt.subplots()
    ax2.barh(df["name"], df["weight"], color="orange")
    ax2.set_xlabel("Berat")
    ax2.set_ylabel("Nama Pokémon")
    st.pyplot(fig2)
    plt.close(fig2)

colC, colD = st.columns(2)

with colC:
    st.write("### Scatter Plot Tinggi vs Berat")
    fig3, ax3 = plt.subplots()
    ax3.scatter(df["height"], df["weight"], color="green")
    ax3.set_xlabel("Tinggi")
    ax3.set_ylabel("Berat")
    st.pyplot(fig3)
    plt.close(fig3)

with colD:
    st.write("### Histogram Jumlah Ability")
    fig4, ax4 = plt.subplots()
    ax4.hist(df["abilities"], bins=range(1, 6), color="purple", rwidth=0.8)
    ax4.set_xlabel("Jumlah Ability")
    ax4.set_ylabel("Frekuensi")
    st.pyplot(fig4)
    plt.close(fig4)
