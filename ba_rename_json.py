import os

carpeta = "json_export"
# Obtener la lista de archivos en la carpeta
archivos = os.listdir(carpeta)
# Recorrer cada archivo en la carpeta
for archivo in archivos:
    if "L_" in archivo:
        indice = archivo.index("L_")
        # Obtener el nuevo nombre del archivo eliminando el texto anterior al "L_"
        nuevo_nombre = archivo[indice:]
        # Ruta completa del archivo original y el nuevo nombre
        ruta_original = os.path.join(carpeta, archivo)
        ruta_nuevo_nombre = os.path.join(carpeta, nuevo_nombre)
        # Renombrar archivo
        os.rename(ruta_original, ruta_nuevo_nombre)
#Success!
print("Success!")