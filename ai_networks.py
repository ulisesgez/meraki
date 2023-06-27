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
    print(data)
    nombre_archivo = os.path.basename(__file__)
    nombre_json = f"{os.path.splitext(nombre_archivo)[0]}.json"
    with open(nombre_json, "w") as archivo:
        json.dump(data, archivo)
    print(f"Archivo JSON guardado: {nombre_json}")
else:
    print("Error en la solicitud:", response.status_code)