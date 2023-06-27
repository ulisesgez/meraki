import aa_var
import requests
import os

url = f'{aa_var.baseURL2}?perPage=1118'

headers = {
    'X-Cisco-Meraki-API-Key': aa_var.key
}

response = requests.get(url, headers=headers)
data = response.json()

network_list = []

for network in data:
    network_obj = {"id": network["id"], "name": network["name"]}
    network_list.append(network_obj)

# Obtener ruta absoluta de carpeta actual:
current_folder = os.path.abspath(os.path.dirname(__file__))
# Construir ruta completa del archivo:
file_path = os.path.join(current_folder, 'ah_networks_id_name.py')

# Guardar la lista en archivo .py:
with open(file_path, 'w') as file:
    file.write("idname = " + repr(network_list))

print('Id y Name de Networks guardadas en el archivo ah_networks_id_name.py.py')