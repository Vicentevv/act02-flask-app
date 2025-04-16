import requests
from flask import Flask
from datetime import datetime
import csv
from io import StringIO

app = Flask(__name__)

# Descargar y procesar el archivo desde la URL
url = "https://gist.githubusercontent.com/reroes/502d11c95f1f8a17d300ece914464c57/raw/872172ebb60e22e95baf8f50e2472551f49311ff/gistfile1.txt"
response = requests.get(url)

personas_filtradas = []

if response.status_code == 200:
    contenido = response.text
    f = StringIO(contenido)
    lector_csv = csv.DictReader(f)

    # Filtrar IDs que empiezan con 3, 4, 5 o 7
    for fila in lector_csv:
        if fila['id'][0] in ['3', '4', '5', '7']:
            personas_filtradas.append(fila)
else:
    print("Error al descargar el archivo:", response.status_code)


@app.route('/')
def home():
    actual = datetime.now()
    fecha_formateada = actual.strftime("%d, %B, %Y, %M, %H, %S")
    return f'¡Hola, LOJA capital cultural! <b>{fecha_formateada}</b>'


@app.route('/personas')
def mostrar_personas():
    if not personas_filtradas:
        return "No hay datos disponibles o hubo un error al descargar."

    tabla_html = """
    <h2>Personas con ID que comienza en 3, 4, 5 o 7</h2>
    <table border="1" cellpadding="5">
        <tr>
            <th>ID</th>
            <th>Nombre</th>
            <th>Edad</th>
        </tr>
    """
    for p in personas_filtradas:
        tabla_html += f"""
        <tr>
            <td>{p['id']}</td>
            <td>{p['nombre']}</td>
            <td>{p['edad']}</td>
        </tr>
        """

    tabla_html += "</table>"
    return tabla_html


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

