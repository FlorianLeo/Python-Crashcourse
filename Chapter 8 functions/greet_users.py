def greet_users_from_a_list(usernames):
	"""Print a simple greeting to each user in a list"""
	for element in usernames:
		print(f"Hello, {element.title()}!")

usernames = ['hannah', 'urs', 'florian', 'holger']
print(greet_users_from_a_list(usernames))