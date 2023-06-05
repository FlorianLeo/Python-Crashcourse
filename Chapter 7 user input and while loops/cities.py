prompt = "\nPlease enter the name of a city you have visited"
prompt += "\nIf you have enough enter 'quit', and the program is stopped."
prompt += "\nYour input: "

while True:
	user_input = input(prompt)
	if user_input == 'quit':
		print("Thanks for watching.\n")
		break
	else:
		print(user_input)