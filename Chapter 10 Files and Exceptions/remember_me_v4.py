"""
Let's refactor greet_user() so it's not doing so many different tasks.
"""
import json

def get_stored_username():
	"""Get stored username if available"""
	filename = 'username.json'
	try:
		with open(filename) as datei:
			username = json.load(datei)
	except FileNotFoundError:
		return None
	else:
		return username

def greet_user():
	"""Greet user by its name"""
	# to greet the user, first the the function retreiving the username is called
	username = get_stored_username()
	if username:
		print(f"Welcome back, {username}!")
	else:
		username = input("What's your name? ")
		filename = 'username.json'
		with open(filename, 'w') as datei:
			json.dump(username, datei)
			print(f"We'll remember yoou when you come back, {username}!")

greet_user()