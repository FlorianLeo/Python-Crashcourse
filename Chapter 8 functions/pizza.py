#Function with 2 Arguments
def show_pizza_topngs(size, *toppings):
	"""Print the list of toppings that have been requested."""
	print(f"\nMaking a {size}-inch Pizza with the following toppings:")
	for element in toppings:
		print(f"\t• {element.title()}")
#Call the Function and pass the parameters
show_pizza_topngs(12, 'peperoni')
show_pizza_topngs(16, 'peperoni', 'mushrooms', 'ham')