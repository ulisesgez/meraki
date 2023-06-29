import aa_var
import requests
import os
import json

url = f'{aa_var.baseURL2}?perPage=2000'

headers = {
    'X-Cisco-Meraki-API-Key': aa_var.key
}

response = requests.get(url, headers=headers)
data = response.json()

network_list = []

for network in data:
    network_obj = {"id": network["id"], "name": network["name"]}
    network_list.append(network_obj)

# Obtener ruta absoluta de la carpeta actual:
current_folder = os.path.abspath(os.path.dirname(__file__))
# Construir la ruta completa del archivo:
file_path = os.path.join(current_folder, 'ai_network_ids_names.py')

# Guardar la lista en el archivo .py con codificación utf-8:
with open(file_path, 'w', encoding='utf-8') as file:
    file.write("idname = " + repr(network_list))

print('Id y Name de Networks guardadas en el archivo ai_network_ids_names.py')