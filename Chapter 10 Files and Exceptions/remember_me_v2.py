import json

# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.
filename = 'username.json'

try:
	with open(filename) as datei:
		username = json.load(datei)
except FileNotFoundError:
	username = input("What is your name? ")
	with open(filename, 'w') as datei:
		json.dump(username, datei)
		print(f"We'll remember you {username} once you return!")
else:
	print(f"Welcome back, {username}.")