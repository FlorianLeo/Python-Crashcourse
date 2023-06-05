def sandwich_items(*zutatenliste):
	"""Print anything that is requested to be in the sandwich"""
	print(f"\nThe Sandwich is filled with:")
	for element in zutatenliste:
		print(f"\t• {element.title()}")

sandwich_items('pastrami', 'dried tomatos', 'pickles')
sandwich_items('ham', 'eggs', 'mayonaise')
sandwich_items('roastbeef', 'salad', 'chumichurri')