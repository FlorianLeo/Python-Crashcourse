import json

def get_stored_username():
	"""Get stored username if available"""
	filename = 'usernames.json'
	try:
		with open(filename) as datei:
			username = json.load(datei)
	except FileNotFoundError:
		return None
	else:
		return username

def get_new_username():
	"""Prompt for a new username"""
	username = input("What's your name? ")
	filename = 'usernames.json'
	with open(filename, 'w') as datei:
		json.dump(username, datei)
	return username

def greet_user():
	"""Greet user by its name"""
	# to greet the user, first the the function retreiving the username is called
	username = get_stored_username()
	if username:
		while True:
			print(f"Welcome back, {username}!")
	else:
		username = get_new_username()
		print(f"We'll remember you when you come back, {username}!")
"""
while True:
	username = get_stored_username()
	if username:
		print(f"Are you {username}?")
		users_answer = input("Answer with 'y' or 'n'")
		if users_answer = 'y':
			greet_user()
		else:
"""

greet_user()