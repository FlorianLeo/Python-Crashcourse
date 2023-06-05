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

get_stored_username()