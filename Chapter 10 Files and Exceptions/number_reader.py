import json

filename = 'numbers.json'

with open(filename) as datei:
	numbers = json.load(datei)

print(numbers)