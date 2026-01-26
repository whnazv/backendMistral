from flask import Flask, request, jsonify, send_from_directory
import requests

LLAMA_SERVER_URL = "http://localhost:8081"

app = Flask(__name__)

# Historial en memoria (simple)
historial = []

@app.route("/", methods=["GET"])
def index():
    return send_from_directory("../frontend", "index.html")

@app.route("/<path:filename>")
def static_files(filename):
    return send_from_directory("../frontend", filename)

@app.route("/v1/completions", methods=["POST"])
def completar():
    global historial
    data = request.get_json()
    user_msg = data.get("prompt", "")

    # Añadir mensaje del usuario al historial
    historial.append(("user", user_msg))

    # Construir prompt completo
    prompt = ""
    for rol, texto in historial:
        if rol == "user":
            prompt += f"<s>[INST] {texto} [/INST]\n"
        else:
            prompt += f"{texto}\n"

    payload = {
        "prompt": prompt,
        "n_predict": 512,
        "temperature": 0.7
    }

    try:
        r = requests.post(f"{LLAMA_SERVER_URL}/completion", json=payload)
        r.raise_for_status()

        respuesta = r.json().get("content", "").strip()

        # Guardar respuesta en historial
        historial.append(("assistant", respuesta))

        return jsonify({
            "choices": [
                {"text": respuesta}
            ]
        })

    except Exception as e:
        print("❌ Error al conectar con llama-server:", e)
        return jsonify({
            "choices": [
                {"text": "Error al generar la respuesta."}
            ]
        }), 500

if __name__ == "__main__":
    print("Servidor Flask en http://localhost:8000")
    app.run(host="0.0.0.0", port=8000)

