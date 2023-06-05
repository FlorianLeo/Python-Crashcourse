print("This is simple addition programm")
print("\nYou can quit by typing 'q'")
first_number = input("The first number please: ")
second_number = input("The second number please: ")
try:
	summary = int(first_number) + int(second_number)
	print(f"The Summary is: {summary}\n")
except ValueError:
	print(f"You Moron - numbers instead of letters\n")