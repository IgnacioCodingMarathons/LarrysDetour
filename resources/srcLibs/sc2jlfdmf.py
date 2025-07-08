# some csv 2 json library for dialogue mode files
import csv,json
csv.field_size_limit(580987875)
def process(f):
    with open(f, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        data = {row[0]: row[1:] for row in reader}
    return json.dumps(data, indent=4)