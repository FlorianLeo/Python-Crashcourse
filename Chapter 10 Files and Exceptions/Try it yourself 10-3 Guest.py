filename = 'guest.txt'

answer_from_user = input("What's your name please: ")

with open(filename, 'a') as file_object:
	file_object.write(f"The Users answer was: {answer_from_user}\n")