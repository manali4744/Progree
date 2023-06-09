import json

input_file = 'font/font_json.json'
output_file = 'json/sort_json.json'

with open(input_file, 'r') as f:
    data = json.load(f)

sorted_data = sorted(data, key=lambda X: X['name'])

# print(sorted_data)

if isinstance(data, list):
    print(len(data), 'list')
elif isinstance(data, dict):
    print(len(data), 'dict')
else:
    print('nthg')
with open(output_file, 'w') as f:
    json.dump(sorted_data, f, indent=4)

print("Json file sorted successfully")