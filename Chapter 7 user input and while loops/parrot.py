prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nIf you have enough enter 'quit', and the program is stopped."
prompt += "\nYour input: "


user_input = ""

#version 1
"""
while user_input != 'quit':
	user_input = input(prompt)
	if user_input != 'quit':
		print(user_input)
	else:
		print("Thanks for watching.\n")
"""

#version 2
the_flag_is_boolean_true = True
while the_flag_is_boolean_true:
	#get the input from the user
	user_input = input(prompt)
	#check if the user has entered quit and thus stop the loop, or keep going
	if user_input == 'quit':
		the_flag_is_boolean_true = False
		print("Thanks for watching.\n")
	else:
		print(user_input)	