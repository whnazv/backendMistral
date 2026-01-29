===========================================================
 README DEL PROYECTO — Chat Local con Llama.cpp + Flask
===========================================================

Este archivo README está completamente dentro de un comentario
Java, tal como solicitaste. Puedes copiarlo tal cual.

-----------------------------------------------------------
🦙 1. DESCRIPCIÓN DEL PROYECTO
-----------------------------------------------------------

Este proyecto permite ejecutar un chat estilo ChatGPT de forma
totalmente local usando:

- llama.cpp como servidor de inferencia (puerto 8081)
- Flask como backend API (puerto 8000)
- Frontend HTML/JS para la interfaz de chat
- Modelos GGUF descargados por el usuario (no incluidos)

El backend recibe mensajes, construye un historial estilo
[INST] ... [/INST], llama al servidor llama.cpp y devuelve la
respuesta al frontend.

-----------------------------------------------------------
📁 2. ESTRUCTURA DEL PROYECTO
-----------------------------------------------------------

backend/
    app.py
frontend/
    index.html
    estilo.css
modelos/
    README.txt   ← instrucciones para descargar modelos
requirements.txt
scripts/
    download_model.py (opcional)

-----------------------------------------------------------
⚙️ 3. INSTALACIÓN DE DEPENDENCIAS
-----------------------------------------------------------

1. Crear entorno virtual (opcional pero recomendado):

    python -m venv venv
    source venv/bin/activate   (Linux/Mac)
    venv\Scripts\activate      (Windows)

2. Instalar dependencias:

    pip install -r requirements.txt

-----------------------------------------------------------
🧠 4. MODELOS (NO INCLUIDOS)
-----------------------------------------------------------

Los modelos NO se incluyen en el repositorio debido a su tamaño.

Debes descargarlos manualmente o mediante un script.

Modelos recomendados (GGUF):

- Mistral 7B Instruct
- Mixtral 8x7B
- Phi-2
- LLaMA 3 Instruct

Descarga desde Hugging Face:
https://huggingface.co/models?search=gguf

Coloca el archivo .gguf dentro de:

    modelos/

-----------------------------------------------------------
🔽 5. DESCARGA AUTOMÁTICA (OPCIONAL)
-----------------------------------------------------------

Si usas un script como scripts/download_model.py:

    python scripts/download_model.py

Este script descargará el modelo y lo guardará en modelos/.

-----------------------------------------------------------
⚡ 6A. COMPILACIÓN DE LLAMA.CPP CON SOPORTE CUDA (OPCIONAL)
-----------------------------------------------------------

Esta sección es SOLO necesaria si deseas compilar llama.cpp
manualmente con aceleración por GPU (CUDA).

Si utilizas binarios precompilados, puedes omitir este paso.

-----------------------------------------------------------
🖥️ REQUISITOS
-----------------------------------------------------------

- GPU NVIDIA compatible con CUDA
- Drivers NVIDIA instalados
- CUDA Toolkit
- Git, CMake, build-essential

-----------------------------------------------------------
📦 1. INSTALAR DEPENDENCIAS BÁSICAS
-----------------------------------------------------------

    sudo apt update
    sudo apt install -y \
        git \
        cmake \
        build-essential \
        python3 \
        python3-pip

-----------------------------------------------------------
🚀 2. INSTALAR CUDA TOOLKIT
-----------------------------------------------------------

Verifica primero que tu GPU es compatible:
https://developer.nvidia.com/cuda-gpus

Instala los drivers NVIDIA (ejemplo):

    sudo apt install -y nvidia-driver-535
    reboot

Instala CUDA Toolkit (ejemplo):

    sudo apt install -y nvidia-cuda-toolkit

Verifica instalación:

    nvcc --version
    nvidia-smi

-----------------------------------------------------------
🦙 3. CLONAR LLAMA.CPP
-----------------------------------------------------------

    git clone https://github.com/ggerganov/llama.cpp.git
    cd llama.cpp

-----------------------------------------------------------
🛠️ 4. COMPILAR LLAMA.CPP CON CUDA
-----------------------------------------------------------

Usando Make (recomendado):

    make clean
    make LLAMA_CUBLAS=1 -j$(nproc)

Alternativa usando CMake:

    mkdir build
    cd build
    cmake .. -DLLAMA_CUBLAS=ON
    cmake --build . --config Release -j$(nproc)

-----------------------------------------------------------
📁 5. BINARIOS GENERADOS
-----------------------------------------------------------

Una vez compilado, encontrarás binarios como:

- llama-server
- llama-cli

Puedes copiarlos a la raíz del proyecto
o añadir la carpeta al PATH del sistema.

-----------------------------------------------------------
✅ 6. VERIFICACIÓN
-----------------------------------------------------------

    ./llama-server --help

Si el comando responde correctamente,
llama.cpp está listo con soporte CUDA.

-----------------------------------------------------------
🚀 7. EJECUTAR EL SERVIDOR DE LLAMA.CPP
-----------------------------------------------------------

Una vez tengas el modelo en modelos/, inicia el servidor:

    ./llama-server \
        -m modelos/tu_modelo.gguf \
        -c 4096 \
        --port 8081

Esto levantará el servidor en:

    http://localhost:8081

-----------------------------------------------------------
🧩 8. EJECUTAR EL BACKEND FLASK
-----------------------------------------------------------

Desde la carpeta backend/:

    python app.py

El backend se iniciará en:

    http://localhost:8000

-----------------------------------------------------------
💬 9. USAR EL CHAT
-----------------------------------------------------------

Abre en tu navegador:

    http://localhost:8000

La interfaz permite:

- Enviar mensajes
- Ver historial
- Recibir respuestas del modelo local

-----------------------------------------------------------
🧠 10. CÓMO FUNCIONA EL BACKEND
-----------------------------------------------------------

El backend:

1. Recibe el mensaje del usuario
2. Lo añade al historial
3. Construye un prompt estilo:
```
<s>[INST] mensaje [/INST]
```
4. Envía el prompt al servidor llama.cpp
5. Recibe la respuesta
6. La devuelve al frontend

Endpoint principal:

    POST /v1/completions

-----------------------------------------------------------
🗂️ 11. NOTAS IMPORTANTES
-----------------------------------------------------------

- El historial se guarda en memoria (no persistente)
- Si reinicias Flask, el historial se borra
- Puedes modificar el formato del prompt según el modelo
- Proyecto pensado para uso local, no producción

-----------------------------------------------------------
🛠️ 12. MEJORAS FUTURAS
-----------------------------------------------------------

- Persistencia del historial
- Soporte para múltiples modelos
- Configuración desde interfaz
- Streaming de tokens
- Descarga automática desde Hugging Face

-----------------------------------------------------------
📜 13. LICENCIA
-----------------------------------------------------------

Este proyecto es libre para uso personal y educativo.

===========================================================
 FIN DEL README
===========================================================

