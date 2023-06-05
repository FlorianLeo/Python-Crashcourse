import json

filename = 'users_favorite_number.json'
user_favorite_number = input("What's your favorite number? ")

with open(filename, 'w') as datei:
	json.dump(user_favorite_number, datei)

with open(filename) as datei:
	user_favorite_number = json.load(datei)
	print(f"I know your favorite number is: {user_favorite_number}")