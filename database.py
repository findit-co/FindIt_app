import csv

def load_resources(csv_file):
    resources = []

    with open(csv_file, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            resources.append(row)

    return resources