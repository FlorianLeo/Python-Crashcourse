"""
We can refactor remember_me_v2.py by moving the bulk of its logic into one or more functions.
The focus of remember_me_v3.py is on greeting the user, so let's move all of our existing
code into a function called greet_user():
This file is a little cleaner, but the function greet_user() is doing more than just greeting
the user - it's also retreiving a stored username if one exists and promtimg for a new username
if one doesn't exist.
"""
import json

def greet_user():
	"""Greet the user by name"""
	filename = 'username.json'
	try:
		with open(filename) as datei:
			username = json.load(datei)
	except FileNotFoundError:
		username = input("What's your name? ")
		with open(filename, 'w') as datei:
			json.dump(username, datei)
			print(f"We'll remember you when you come back, {username}")
	else:
		print(f"Welcome back, {username}!")

greet_user()