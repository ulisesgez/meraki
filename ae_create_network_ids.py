import aa_var
import requests
import json
import os

url = f'{aa_var.baseURL2}?perPage=2000'

headers = {
    'X-Cisco-Meraki-API-Key': aa_var.key
}

response = requests.get(url, headers=headers)
data = response.json()

network_ids = []

for network in data:
    network_ids.append(network['id'])

# Obtener ruta absoluta de carpeta actual:
current_folder = os.path.abspath(os.path.dirname(__file__))
# Construir ruta completa del archivo:
file_path = os.path.join(current_folder, 'af_network_ids.py')
# Guardar el array en archivo:
with open(file_path, 'w') as file:
    file.write(f'ids = {json.dumps(network_ids)}')
print('Network ids almacenadas en el archivo af_network_ids.py')