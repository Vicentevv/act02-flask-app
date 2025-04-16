import requests

url = "https://gist.githubusercontent.com/reroes/502d11c95f1f8a17d300ece914464c57/raw/872172ebb60e22e95baf8f50e2472551f49311ff/gistfile1.txt"
response = requests.get(url)

if response.status_code == 200:
    print("Contenido descargado:")
    print(response.text)
else:
    print(f"Error al acceder a la URL: {response.status_code}")
