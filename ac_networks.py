import aa_var
import requests
import json
import os

url = f"{aa_var.baseURL2}"
headers = {
    "X-Cisco-Meraki-API-Key": aa_var.key
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    # Imprimir el JSON con formato
    print(json.dumps(data, indent=4))
    
    guardar_json = input("¿Desea guardar el archivo JSON? (y/n): ")
    if guardar_json.lower() == "y":
        # Obtener ruta de la carpeta "jsons"
        ruta_carpeta = os.path.join(os.path.dirname(__file__), "jsons")
        # Verificar si la carpeta no existe y crearla en caso necesario
        if not os.path.exists(ruta_carpeta):
            os.makedirs(ruta_carpeta)
        # Generar nombre del archivo JSON
        nombre_json = os.path.join(ruta_carpeta, "networks.json")
        # Guardar datos de respuesta en un archivo JSON
        with open(nombre_json, "w") as archivo:
            json.dump(data, archivo)
        print(f"Archivo JSON guardado: {nombre_json}")
else:
    print("Error en la solicitud:", response.status_code)