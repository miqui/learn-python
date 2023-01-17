import json

# Open the file
with open('file.json', 'r') as f:
    # Load the JSON data from the file
    data = json.load(f)

# Access the data as a Python object
print(data)
