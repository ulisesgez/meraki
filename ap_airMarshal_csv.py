import os
import json
import csv

input_directory = "./jsons/wireless/air_marshal"
output_directory = "./csvs/wireless/air_marshal"

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

columns = ['id', 'name', 'ssid', 'bssids', 'device', 'channels', 'firstSeen', 'lastSeen']
csv_data = []

total_files = len([filename for filename in os.listdir(input_directory) if filename.endswith('.json')])

json_count = 0
csv_count = 0

for filename in os.listdir(input_directory):
    if filename.endswith('.json'):
        json_count += 1

        with open(os.path.join(input_directory, filename), 'r', encoding='utf-8') as file:
            data = json.load(file)

        if isinstance(data, list):
            for item in data:
                if 'channels' in item:
                    channels = item['channels']
                    if isinstance(channels, str):
                        channels = channels.replace(',', '-')
                        item['channels'] = channels

                bssids = ', '.join([bssid['bssid'] for bssid in item.get('bssids', [])])
                devices = ', '.join([device['device'] for bssid in item.get('bssids', []) for device in bssid.get('detectedBy', [])])

                row_data = {column: item.get(column, '') for column in columns}
                row_data['bssids'] = bssids
                row_data['device'] = devices

                csv_data.append(row_data)

        if json_count % 15 == 0 or json_count == total_files:
            csv_count += 1
            csv_filename = f'csv{csv_count}.csv'
            csv_path = os.path.join(output_directory, csv_filename)
            with open(csv_path, 'w', newline='', encoding='utf-8') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=columns)
                writer.writeheader()
                writer.writerows(csv_data)
                csv_data = []

        progress = int((json_count / total_files) * 100)
        progress_str = f'[{progress}%]'
        print(f'\rProgress: {progress_str}', end='')

print("\nSuccess")