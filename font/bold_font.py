import os
import json

folder_path = '/home/pc/Documents/demo_try_error/font/Font Pack'
file = os.listdir(folder_path)

ttf_files = [f for f in file if f.endswith('.ttf')]

file_list = []

# validate = ['bold', 'italic', 'oblique']
for file_name in ttf_files:
    # Check if the file name contains the word "bold" (case insensitive)
    if 'bold' not in file_name.lower() or 'italic' not in file_name.lower() or 'oblique' not in file_name:
        file_path = os.path.join(folder_path, file_name)
        file_info = {
            'name': os.path.splitext(file_name)[0],
            'path': file_path
        }
        file_list.append(file_info)

output_file = 'json/font_json_bold.json'

with open(output_file, 'w') as f:
    json.dump(file_list, f, indent=4)

print('JSON file created successfully.')
