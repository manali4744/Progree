import json

# Define the path to your JSON file and the output text file
JSON_FILE = "ambignq_light/dev_light.json"
OUTPUT_FILE = "output.txt"

# Read the JSON data from the file
with open(JSON_FILE, "r") as json_file:
    data_list = json.load(json_file)

# Open the output text file for writing
with open(OUTPUT_FILE, "w") as output_file:
    for data in data_list:
        question = data["question"]
        answer = data["annotations"][0]["answer"][0]  # Assuming you want the first answer
        output_file.write(f'("{question}" "{answer}")\n')

print("Data written to", OUTPUT_FILE)

