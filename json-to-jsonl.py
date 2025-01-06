import json

# Load JSON file
with open('dataset.jsonl', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Write JSONL file
with open('main-dataset.jsonl', 'w', encoding='utf-8') as jsonl_file:
    for entry in data:
        jsonl_file.write(json.dumps(entry, ensure_ascii=False) + '\n')

print("Conversion completed. JSONL file created.")

