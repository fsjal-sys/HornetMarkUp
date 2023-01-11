import yaml
import matplotlib.pyplot as plt

def clean_yaml(data):
    cleaned_data = {}
    for key, value in data.items():
        if value is not None:
            cleaned_data[key] = value
    return cleaned_data

def transform_yaml(data):
    transformed_data = {}
    for key, value in data.items():
        if isinstance(value, dict):
            transformed_data[key] = {**value, "new_field": len(value["existing_field"])}
        else:
            transformed_data[key] = value
    return transformed_data

def visualize_yaml(data):
    values = [v["new_field"] for k, v in data.items() if isinstance(v, dict)]
    plt.bar(range(len(values)), values)
    plt.show()

# Load the YAML file
try:
    with open('data.yaml', 'r') as f:
        data = yaml.safe_load(f)
except FileNotFoundError:
    # Handle missing file
    print('data.yaml file not found')
    exit(1)
except yaml.YAMLError as e:
    # Handle invalid YAML
    print(f"Invalid YAML file {e}")
    exit(1)

# Clean the data
data = clean_yaml(data)

# Transform the data
data = transform_yaml(data)

# Visualize the data
visualize_yaml(data)
