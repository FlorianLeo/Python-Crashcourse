print("This is simple addition programm")

while True:
	print("\nYou can quit by typing 'q'")
	first_number = input("The first number please: ")
	if first_number == 'q':
		break
	second_number = input("The second number please: ")
	if second_number == 'q':
		break
	try:
		summary = int(first_number) + int(second_number)
		print(f"The Summary is: {summary}\n")
	except ValueError:
		print(f"You Moron - numbers instead of letters\n")