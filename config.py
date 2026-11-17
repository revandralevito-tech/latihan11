
import os
from pathlib import Path

from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env", encoding="utf-8")


def _get_int(name: str, default: int) -> int:
    """Ambil variabel .env sebagai bilangan bulat; pakai default jika kosong/salah."""
    value = os.getenv(name, "").strip()
    try:
        return int(value) if value else default
    except ValueError:
        print(f"[config] {name}={value!r} bukan angka, memakai nilai bawaan {default}.")
        return default


APP1_TITLE = os.getenv("APP1_TITLE", "Visualisasi Data Penjualan dari Excel dengan Matplotlib")
EXCEL_FILE = BASE_DIR / os.getenv("EXCEL_FILE", "penjualan.xlsx")

APP2_TITLE = os.getenv("APP2_TITLE", "Visualisasi Data Pokémon")
POKEAPI_URL = os.getenv("POKEAPI_URL", "https://pokeapi.co/api/v2/pokemon")
POKEMON_MIN = _get_int("POKEMON_MIN", 5)
POKEMON_MAX = _get_int("POKEMON_MAX", 30)
POKEMON_DEFAULT = _get_int("POKEMON_DEFAULT", 10)
REQUEST_TIMEOUT = _get_int("REQUEST_TIMEOUT", 10)

if POKEMON_MIN < 1:
    POKEMON_MIN = 1
if POKEMON_MAX < POKEMON_MIN:
    POKEMON_MAX = POKEMON_MIN
POKEMON_DEFAULT = min(max(POKEMON_DEFAULT, POKEMON_MIN), POKEMON_MAX)
