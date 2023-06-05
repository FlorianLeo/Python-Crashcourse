import json

filename = 'username.json'

with open(filename) as datei:
	username = json.load(datei)
	print(f"Welcome back {username}!")