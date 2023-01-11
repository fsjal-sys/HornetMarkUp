import json
import matplotlib.pyplot as plt

def clean_json(data):
    cleaned_data = []
    for record in data:
        cleaned_record = {k: v for k, v in record.items() if v is not None}
        cleaned_data.append(cleaned_record)
    return cleaned_data

def transform_json(data):
    transformed_data = []
    for record in data:
        try:
            record["new_field"] = len(record["existing_field"])
        except KeyError:
            # Handle missing "existing_field" key
            print(f'Missing key in the record: {record}')
        transformed_data.append(record)
    return transformed_data

def visualize_json(data):
    values = [record["new_field"] for record in data]
    plt.bar(range(len(values)), values)
    plt.show()

# Load the JSON file
try:
    with open('data.json', 'r') as f:
        data = json.load(f)
except FileNotFoundError:
    # Handle missing file
    print('data.json file not found')
    exit(1)
except json.decoder.JSONDecodeError:
    # Handle invalid JSON
    print('Invalid JSON file')
    exit(1)

# Clean the data
data = clean_json(data)

# Transform the data
data = transform_json(data)

# Visualize the data
if len(data) > 0:
    visualize_json(data)
else:
    print("Data is empty, nothing to visualize")
