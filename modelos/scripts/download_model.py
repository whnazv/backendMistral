#!/usr/bin/env python3
import os
from huggingface_hub import hf_hub_download

# Modelo por defecto (puedes cambiarlo)
REPO_ID = "TheBloke/Mistral-7B-Instruct-v0.2-GGUF"
FILENAME = "mistral-7b-instruct-v0.2.Q4_K_M.gguf"

# Carpeta "modelos" (un nivel arriba del script)
DEST_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def main():
    print("📥 Descargando modelo desde Hugging Face...")
    print(f"Repositorio: {REPO_ID}")
    print(f"Archivo: {FILENAME}")

    os.makedirs(DEST_DIR, exist_ok=True)

    ruta = hf_hub_download(
        repo_id=REPO_ID,
        filename=FILENAME,
        local_dir=DEST_DIR
    )

    print(f"✅ Modelo descargado en: {ruta}")

if __name__ == "__main__":
    main()

