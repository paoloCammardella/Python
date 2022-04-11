import json

with open('prova.json') as jsonF:
    data = json.load(jsonF)


# print(json.dumps(data, indent = 4, sort_keys = True))
print(data)