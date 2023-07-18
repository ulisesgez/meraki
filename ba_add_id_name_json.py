import os
import json
from ai_network_ids_names import idname

# Ruta de la carpeta que contiene los archivos JSON
carpeta = "./jsons/wireless/air_marshal"

# Iterar sobre cada archivo en la carpeta
for archivo in os.listdir(carpeta):
    if archivo.endswith('.json'):
        # Obtener el ID del archivo
        id_archivo = os.path.splitext(archivo)[0]
        
        # Buscar el nombre correspondiente en el array idname
        nombre_archivo = None
        for item in idname:
            if item['id'] == id_archivo:
                nombre_archivo = item['name']
                break
        
        if nombre_archivo:
            # Leer el archivo JSON
            ruta_archivo = os.path.join(carpeta, archivo)
            with open(ruta_archivo, 'r') as f:
                contenido = json.load(f)
            
            # Añadir los campos id y name a cada diccionario
            for diccionario in contenido:
                diccionario['id'] = id_archivo
                diccionario['name'] = nombre_archivo
            
            # Guardar el archivo actualizado
            with open(ruta_archivo, 'w') as f:
                json.dump(contenido, f, indent=4)
            
            print(f"Se añadieron los campos id y name al archivo: {archivo}")
        else:
            print(f"No se encontró el nombre correspondiente para el ID {id_archivo}")