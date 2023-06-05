import json

username = input("What is your name? ")

filename = 'username.json'

with open(filename, 'w') as datei:
	json.dump(username, datei)
	print(f"We'll remember you {username} once you return.")