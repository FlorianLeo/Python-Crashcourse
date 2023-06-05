"""
Let's refactor it again. Each function in this final version of remember_me_v5.py has
a single, clear prupose. We call greet_user(), and that function prints the appropriate message:
it either welcomes back an existing user or greets a new user. It does this by calling get_stored_username(),
which is responsible only for retrieving a store username if one exists. Finally, greet_user() calls
get_new_username() if necessary, which is responsible only for getting a new username and storing it.
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

def get_new_username():
	"""Prompt for a new username"""
	username = input("What's your name? ")
	filename = 'username.json'
	with open(filename, 'w') as datei:
		json.dump(username, datei)
	return username

def greet_user():
	"""Greet user by its name"""
	# to greet the user, first the the function retreiving the username is called
	username = get_stored_username()
	if username:
		print(f"Welcome back, {username}!")
	else:
		username = get_new_username()
		print(f"We'll remember you when you come back, {username}!")

greet_user()