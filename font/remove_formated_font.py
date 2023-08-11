import os
import json
from fontTools.ttLib import TTFont

folder_path = '/home/pc/Documents/demo_try_error/font/Font Pack'
file = os.listdir(folder_path)

ttf_files = [f for f in file if f.endswith('.ttf')]

file_list = []

for file_name in ttf_files:
    file_path = os.path.join(folder_path, file_name)
    try:
        font = TTFont(file_path)
        is_regular = all('Regular' in name for name in font.getNames())
        if is_regular:
            file_info = {
                'name': os.path.splitext(file_name)[0],
                'path': file_path
            }
            file_list.append(file_info)
    except Exception as e:
        print(f"Error processing {file_name}: {e}")

output_file = 'json/font_json_demo.json'

with open(output_file, 'w') as f:
    json.dump(file_list, f, indent=4)

print('JSON file created successfully.')
