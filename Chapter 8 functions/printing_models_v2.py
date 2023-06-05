def print_models(still_to_do, already_done):
	"""
	simulate printing each design, until none are left.
	move each design to already_done after printing.
	"""
	while still_to_do:
		current_design = still_to_do.pop()
		print(f"Printing model: {current_design}")
		already_done.append(current_design)

def show_completed_models(already_done):
	"""show all models that were printed"""
	print("\nThe following models have been printed:")
	for element in already_done:
		print(f"• {element}")

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)