import aa_var
import requests
import json
import os

url = f"{aa_var.baseURL3}/{aa_var.id}/wireless/airMarshal"
headers = {
    "X-Cisco-Meraki-API-Key": aa_var.key
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    formatted_data = json.dumps(data, indent=4)
    print(formatted_data)

    # Obtener el ID del archivo desde la ruta
    id_archivo = aa_var.id

    # Obtener la ruta de la carpeta "jsons"
    ruta_jsons = os.path.join(os.path.dirname(__file__), "jsons")

    # Verificar si la carpeta "jsons" no existe y crearla en caso necesario
    if not os.path.exists(ruta_jsons):
        os.makedirs(ruta_jsons)

    # Obtener la ruta de la carpeta "airMarshal" dentro de "jsons"
    ruta_carpeta = os.path.join(ruta_jsons, "wireless", "air_marshal")

    # Verificar si la carpeta "airMarshal" no existe y crearla en caso necesario
    if not os.path.exists(ruta_carpeta):
        os.makedirs(ruta_carpeta)

    # Generar el nombre del archivo JSON con el ID
    nombre_json = os.path.join(ruta_carpeta, f"{id_archivo}.json")

    # Preguntar al usuario si desea guardar el archivo
    respuesta = input("¿Desea guardar el archivo? y/n: ")

    if respuesta.lower() == "y":
        # Guardar datos de respuesta en un archivo JSON (reemplazar si ya existe)
        with open(nombre_json, "w") as archivo:
            json.dump(data, archivo)
        print(f"Archivo JSON guardado: {nombre_json}")
    else:
        print("El archivo no será guardado.")

    print(f"Éxito en la solicitud de la API: {response.status_code}")
else:
    print("Error en la solicitud:", response.status_code)