import requests
from flask import Flask
from datetime import datetime

# Descargamos el contenido al iniciar el programa
url = "https://gist.githubusercontent.com/reroes/502d11c95f1f8a17d300ece914464c57/raw/872172ebb60e22e95baf8f50e2472551f49311ff/gistfile1.txt"
response = requests.get(url)

if response.status_code == 200:
    print("Contenido descargado:")
    print(response.text)
else:
    print(f"Error al acceder a la URL: {response.status_code}")

# Creamos la app Flask
app = Flask(__name__)

@app.route('/')
def home():
    actual = datetime.now()
    fecha_formateada = actual.strftime("%d, %B, %Y, %M, %H, %S")
    return f'¡Hola, LOJA capital cultural! <b>{fecha_formateada}</b>'

# Ejecutamos el servidor
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
