import aa_var
import requests
import json
import os

url = f'{aa_var.baseURL2}?perPage=1118'
headers = {
    "X-Cisco-Meraki-API-Key": aa_var.key
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    network_list = []  # Lista para almacenar los objetos de las networks

    for network in data:
        network_obj = {"id": network["id"], "name": network["name"]}
        network_list.append(network_obj)

    print(network_list)

    nombre_archivo = os.path.basename(__file__)
    nombre_json = f"{os.path.splitext(nombre_archivo)[0]}.json"

    with open(nombre_json, "w") as archivo:
        json.dump(network_list, archivo)

    print(f"Archivo JSON guardado: {nombre_json}")
else:
    print("Error en la solicitud:", response.status_code)