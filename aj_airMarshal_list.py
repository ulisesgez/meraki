from ad_network_ids import ids
import aa_var
import requests
import json
import os

# Crear la carpeta si no existe
carpeta_export = "json_export"
if not os.path.exists(carpeta_export):
    os.makedirs(carpeta_export)

# Iterar sobre cada ID
for id in ids:
    url = f"{aa_var.baseURL3}/{id}/{aa_var.baseURL4}"
    headers = {
        "X-Cisco-Meraki-API-Key": aa_var.key
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        print(data)
        nombre_archivo = os.path.basename(__file__)
        nombre_json = f"{os.path.splitext(nombre_archivo)[0]}_{id}.json"
        with open(os.path.join(carpeta_export, nombre_json), "w") as archivo:
            json.dump(data, archivo)
        print(f"Archivo JSON guardado: {nombre_json}")
    else:
        print("Error en la solicitud:", response.status_code)