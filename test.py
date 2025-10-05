import json

with open('labs\\infolab1\\datal.json', 'r') as file:
    loaded = json.load(file)

kys = list(loaded.keys())

for k in kys:
    if '11' in loaded[k]:
        print(True)
