import json

def get_stored_favorite_number():
	"""If file available return the content of the file"""
	filename = 'users_favorite_number.json'
	try:
		with open(filename) as datei:
			user_favorite_number = json.load(datei)
	except FileNotFoundError:
		return None
	else:
		return user_favorite_number

def store_favorite_number():
	"""Ask user for a favorite number and store it in a file"""
	filename = 'users_favorite_number.json'
	user_favorite_number = input("What's your favorite number? ")
	with open(filename, 'w') as datei:
		json.dump(user_favorite_number, datei)
	return user_favorite_number

def favorite_number():
	"""Either show a favorite number, or ask for one and store it"""
	user_favorite_number = get_stored_favorite_number()
	if user_favorite_number:
		print(f"I know your favorite number is: {user_favorite_number}")
	else:
		user_favorite_number = store_favorite_number()
		print(f"Your number {user_favorite_number} has been saved for future use.")

favorite_number()