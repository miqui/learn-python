import csv
import json

# Open the JSON file
with open("input.json", "r") as json_file:
    data = json.load(json_file)

# Open the CSV file
with open("output.csv", "w", newline="") as csv_file:
    # Create a CSV writer
    writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())

    # Write the column names
    writer.writeheader()

    # Write the data rows
    for row in data:
        writer.writerow(row)
