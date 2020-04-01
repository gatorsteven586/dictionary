import json
filename = 'storage.json'

with open(filename) as f:
    stored = json.load(f)
# stored = {}
addfirst = input('First: ')
addlast = input('Last: ')
stored[addfirst] = addlast
print(stored)

with open(filename, 'w') as f:
    json.dump(stored, f)