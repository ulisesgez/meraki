from ad_network_ids import ids
import aa_var
import requests
import json
import os
import time

# Crear la carpeta si no existe
carpeta_export = "json_export"
if not os.path.exists(carpeta_export):
    os.makedirs(carpeta_export)

def obtener_estado_actual():
    estado_actual = 0
    if os.path.isfile("estado.txt"):
        with open("estado.txt", "r") as archivo:
            estado_actual = int(archivo.read())
    return estado_actual

def actualizar_estado_actual(estado_actual):
    with open("estado.txt", "w") as archivo:
        archivo.write(str(estado_actual))

# Obtener estado actual
estado_actual = obtener_estado_actual()
print(f"Estado actual: {estado_actual}")

# Iterar sobre cada ID a partir del estado actual
for i in range(estado_actual, len(ids)):
    id = ids[i]
    url = f"{aa_var.baseURL3}/{id}/{aa_var.baseURL4}"
    headers = {
        "X-Cisco-Meraki-API-Key": aa_var.key
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        data = response.json()
        print(data)
        nombre_json = f"L_{id}.json"
        if id.startswith("L_"):
            nombre_json = f"{id}.json"
        with open(os.path.join(carpeta_export, nombre_json), "w") as archivo:
            json.dump(data, archivo)
        print(f"Archivo JSON guardado: {nombre_json}")
        # Actualizar el estado actual
        actualizar_estado_actual(i + 1)
    except requests.exceptions.RequestException as e:
        print("Error en la solicitud:", str(e))
    # Esperar un tiempo entre iteraciones:
    time.sleep(1)