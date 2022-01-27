import csv
import json

cluster = {
    "component": 1,
    "database": 2,
    "extension": 3,
    "environment": 4,
    "language": 5,
    "library": 3,
    "platform": 6,
    "subsystem": 7,
    "system": 7,
    "framework": 3,
    "ide": 4,
    "tool": 8,
    "toolkit": 8,
    "utility": 8
}

def generate_json(language):
    children = [ ]
    with open(language + '.csv', 'r') as file:
        reader = csv.reader(file)
        headers = next(reader, None)
        rows = []
        cluster_list = []
        for row in reader:
            rows.append(row)

        for i in range (1, 9):
            temp_list = []
            for row in rows:
                if cluster[row[2]] == i:
                    temp_list.append(row)

            temp_list.sort(key=lambda v: v[2])
            cluster_list.append(temp_list)

        flat_list = [item for sublist in cluster_list for item in sublist]

        for row in flat_list:
            children.append( { "name": row[0], "group": row[2] } )

    json_string = { "name": language, "group": "language", "children": children }
    with open(language + '_json_data.json', 'w') as outfile:
        json.dump(json_string, outfile)

generate_json("csharp")
generate_json("java")
generate_json("javascript")
generate_json("php")
generate_json("python")