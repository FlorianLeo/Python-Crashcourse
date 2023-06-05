filename = 'like_programming.txt'

print("Give your name and describe why you like programming")
while True:
	print("\nYou can quit by typing 'q'")
	ask_username = input("What's you name: ")
	if ask_username == 'q':
		break
	ask_programming = input("What do you like about programming: ")
	if ask_programming == 'q':
		with open(filename, 'a') as file_object:
			file_object.write(f"The user {ask_username} did not answer the question.\n")
		break
	with open(filename, 'a') as file_object:
		file_object.write(f"The user {ask_username} sayed: '{ask_programming}'\n")