number = input("Enter a number, and make sure it is even: ")
number = int(number)

if number % 2 == 0:
	print(f"\nThe number {number} you entered is indeed even. Well done!")
else:
	print(f"\nThe number {number} is odd. Too bad!")