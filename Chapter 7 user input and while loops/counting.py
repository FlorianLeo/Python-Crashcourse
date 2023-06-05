counter = 0
print(f"The counter value before the while loop is started: {counter}")
print("The while loop is meant to run until the counter is less or equal to five")
print("Now - lets start the while loop, and print some messages\n")
while counter <= 5:
	print(f"Right now the while loop is doing its {counter + 1}. run.")
	print(f"The value of the counter at this point is {counter}, though")
	print(f"Next - the counter is imcremented by 1.")
	counter += 1
	print(f"The value of the counter is: {counter} now.\n")