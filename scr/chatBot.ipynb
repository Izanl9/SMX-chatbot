from flask import Flask, request, jsonify
from pyngrok import ngrok
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import google.generativeai as genai
from flask_cors import CORS
from google.colab import userdata
!kill -9 $(lsof -t -i:5001)
# ==============================
# CONFIGURACIÓN DE LA API
# ==============================
GOOGLE_API_KEY = userdata.get("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    print("⚠️ No se ha encontrado la clave API. Configúrala antes de ejecutar el programa.")
genai.configure(api_key=GOOGLE_API_KEY)

# ==============================
# CONFIGURACIÓN DE FLASK
# ==============================
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# ==============================
# CONFIGURACIÓN DE NGROK
# ==============================
NGROK_AUTHTOKEN = userdata.get("NGROK")
ngrok.set_auth_token(NGROK_AUTHTOKEN)
public_url = ngrok.connect(5001)
print(f" * Servidor disponible en: {public_url}")

# ==============================
# FUNCIÓN DE SCRAPING RECURSIVO EN TODA LA WEB
# ==============================
def obtener_info_web(url, visitadas=set()):
    print(f"Scraping página: {url}")
    if url in visitadas:
        return ""

    try:
        respuesta = requests.get(url, timeout=10)
        respuesta.raise_for_status()
        soup = BeautifulSoup(respuesta.text, "html.parser")
        visitadas.add(url)

        # Extraer información de la página actual
        titulo = soup.title.string if soup.title else "Sin título"
        parrafos = [p.text for p in soup.find_all("p")]
        contenido = f"Título: {titulo}\nContenido: {' '.join(parrafos[:50])}"

        # Buscar enlaces internos y hacer scraping en ellos
        enlaces = [urljoin(url, a['href']) for a in soup.find_all('a', href=True) if urljoin(url, a['href']).startswith("https://ilecina.inscastellbisbal.net")]
        for enlace in enlaces:
            contenido += "\n" + obtener_info_web(enlace, visitadas)

        return contenido
        print('scraping finalizado')
    except Exception as e:
        return f"Error al obtener datos de la web: {e}"

# ==============================
# INSTRUCCIONES DEL SISTEMA
# ==============================
system_instruction = """
Ets un assistent d'intel·ligència artificial que utilitza informació de la web ilecina.inscastellbisbal.net,
Proporciona respostes clares i basades únicament en les dades proporcionades, omet tot sobre els gustos i no mencionis molt el repte1, sóc izan.
"""

# Crear el chat
chat = genai.GenerativeModel("gemini-1.5-flash").start_chat()

@app.route('/', methods=['POST'])
def obtener_respuesta():
    if request.method == "OPTIONS":
        return jsonify({"status": "ok"}), 200

    try:
        data = request.get_json()
        if not data or 'mensaje' not in data:
            return jsonify({'error': 'Solicitud inválida, falta "mensaje"'}), 400

        mensaje = data['mensaje']
        # Imprimir el mensaje recibido en los logs de Flask
        print(f"Mensaje recibido: {mensaje}")

        # Obtener información de toda la web
        info_web = obtener_info_web("https://ilecina.inscastellbisbal.net")

        # Enviar mensaje al modelo con la información extraída
        respuesta = chat.send_message(f"{info_web}\n\nPregunta: {mensaje}")

        print(f"Respuesta del modelo: {respuesta.text.strip()}")

        return jsonify({'respuesta': respuesta.text.strip()}), 200
        print('funciona')

    except Exception as e:
        # Capturar cualquier error y mostrarlo en los logs
        print(f"Error al procesar la solicitud: {e}")
        return jsonify({'error': 'Error interno en el servidor'}), 500

obtener_info_web('https://ilecina.inscastellbisbal.net')
if __name__ == '__main__':
    app.run(port=5001)
