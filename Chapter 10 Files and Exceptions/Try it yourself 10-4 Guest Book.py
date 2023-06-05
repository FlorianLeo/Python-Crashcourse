filename = 'guest_book.txt'

while True:
	print("\nYou can quit any time by typing 'q'")
	ask_username = input("Your name, please: ")
	if ask_username == 'q':
		break
	else:
		with open(filename, 'a') as file_object:
			file_object.write(f"The answer was: {ask_username}\n")