def get_formatted_name(first_name, last_name):
	"""Return a full name, neatly formatted"""
	#When a function returns something, a variable must be provided to hold it
	full_name = f"{first_name} {last_name}"
	return full_name.title()

while True:
	print("\nPlease provide your name:")
	print("You may quit at any time by typing 'q'")
	ask_first_name = input("First Name: ")
	if ask_first_name == 'q':
		break
	ask_last_name = input("Last Name: ")
	if ask_last_name == 'q':
		break
	print(f"\nHello, {get_formatted_name(ask_first_name, ask_last_name)}!")