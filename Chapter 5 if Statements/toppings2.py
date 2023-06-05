requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':
		print("Sorry, we are aout of green peppers")
	else:
		print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")