import aa_var
import requests
import json
import os

url = f"{aa_var.baseURL3}/{aa_var.id}/wireless/airMarshal?timespan=2678400"
headers = {
    "X-Cisco-Meraki-API-Key": aa_var.key
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    formatted_data = json.dumps(data, indent=4)
    print(formatted_data)
    # Obtener nombre del archivo actual
    nombre_archivo = os.path.basename(__file__)
    # Obtener ruta de la carpeta "jsons"
    ruta_carpeta = os.path.join(os.path.dirname(__file__), "jsons")
    # Verificar si la carpeta no existe y crearla en caso necesario
    if not os.path.exists(ruta_carpeta):
        os.makedirs(ruta_carpeta)
    # Generar nombre del archivo JSON
    nombre_json = os.path.join(ruta_carpeta, f"{os.path.splitext(nombre_archivo)[0]}.json")
    # Guardar datos de respuesta en un archivo JSON
    with open(nombre_json, "w") as archivo:
        json.dump(data, archivo)
    print(f"Éxito en la solicitud de la API: {response.status_code}")
    print(f"Archivo JSON guardado: {nombre_json}")
else:
    print("Error en la solicitud:", response.status_code)