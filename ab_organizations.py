import aa_var
import requests
import json

url = f"{aa_var.baseURL1}"
headers = {
    "X-Cisco-Meraki-API-Key": aa_var.key
}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    formatted_data = json.dumps(data, indent=4)
    print(formatted_data)
    print(f"Éxito en la solicitud de la API: {response.status_code}")
else:
    print("Error en la solicitud:", response.status_code)