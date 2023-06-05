pizza = {
	'crust':'thick',
	'toppings':['mushrooms', 'cheese', 'tomatosauce', 'extra cheese', 'extra tomatosauce', 'ham', 'bacon']
}

print(f"You ordered a Pizza with a crust that is {pizza['crust']} with the following toppings")

for element in pizza['toppings']:
	print(f'\t{element.title()}')