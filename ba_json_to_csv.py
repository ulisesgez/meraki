import pandas as pd
import glob
import os

# Ruta JSONS
json_files = glob.glob("jsons/*.json")
total_files = len(json_files)
processed_files = 0

# Verificar y crear directorio de exportación
if not os.path.exists("export"):
    os.makedirs("export")

# Dividir en lotes más pequeños
batch_size = 10
batch_files = [json_files[i:i+batch_size] for i in range(0, len(json_files), batch_size)]

# Procesar archivos y guardar en CSV
batch_csv_files = []
for batch_num, batch in enumerate(batch_files, 1):
    batch_dfs = []
    for file in batch:
        with open(file, 'r') as f:
            for chunk in pd.read_json(f, orient='records', lines=True, chunksize=1000):
                batch_dfs.append(chunk)
        processed_files += 1
        percentage = (processed_files / total_files) * 100
        if processed_files % batch_size == 0:
            print(f"Progreso: {percentage:.2f}%")

    batch_df = pd.concat(batch_dfs)
    batch_csv_file = f"export/batch_{batch_num * batch_size}.csv"
    batch_csv_files.append(batch_csv_file)
    with open(batch_csv_file, 'w') as f:
        batch_df.to_csv(f, index=False)

    del batch_dfs
    del batch_df

print("Todos los lotes procesados y guardados en archivos CSV")

# Combinar archivos CSV en un solo DataFrame
combined_df = pd.concat([pd.read_csv(csv_file) for csv_file in batch_csv_files], ignore_index=True)

# Ruta CSV
csv_file = "export/combined_data.csv"
# Ruta Excel
excel_file = "export/combined_data.xlsx"

# Guardar DataFrame combinado en archivo CSV
with open(csv_file, 'w') as f:
    combined_df.to_csv(f, index=False)
print("Archivo CSV guardado en:", csv_file)

# Guardar DataFrame combinado en archivo Excel si es posible
if combined_df.shape[0] <= 1048576 and combined_df.shape[1] <= 16384:
    combined_df.to_excel(excel_file, index=False)
    print("Archivo Excel guardado en:", excel_file)
else:
    print("El tamaño del DataFrame combinado excede los límites de Excel. Generando archivos adicionales...")

    # Generar archivos adicionales
    chunk_size = 1048576
    num_chunks = (combined_df.shape[0] - 1) // chunk_size + 1

    writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')
    for i in range(num_chunks):
        chunk_start = i * chunk_size
        chunk_end = min((i + 1) * chunk_size, combined_df.shape[0])
        chunk_df = combined_df.iloc[chunk_start:chunk_end]
        sheet_name = f"Sheet{i+1}"
        chunk_df.to_excel(writer, sheet_name=sheet_name, index=False)

    writer.save()
    writer.close()

    print("Archivos Excel generados")