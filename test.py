import json

with open('db.json', 'r+') as file:
    test = json.load(file)
    test.append({'name': 'Sudip', 'Amount': '100'})
    json.dump(test, file)