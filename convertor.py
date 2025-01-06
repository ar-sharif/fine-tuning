import json

# Load original JSONL file
with open("training_data.jsonl", "r", encoding="utf-8") as file:
    lines = file.readlines()

# Convert to new format
converted_data = []
for line in lines:
    record = json.loads(line)
    converted_data.append({
        "instruction": "Rewrite with improvements.",
        "input": record["previous_description"],
        "output": record["description"]
    })

# Save to new JSONL
with open("converted_training_data.jsonl", "w", encoding="utf-8") as file:
    for record in converted_data:
        file.write(json.dumps(record, ensure_ascii=False) + "\n")

