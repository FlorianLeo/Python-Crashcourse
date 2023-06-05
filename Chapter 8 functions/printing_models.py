# Start with some designs that need to be printed.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each design, until none are left.
# Move each design to completed_models after printing.
while unprinted_designs:
	current_design = unprinted_designs.pop()
	print(f"Printing model: {current_design}")
	completed_models.append(current_design)

# Display all completed models.
print(f"\nThe following models have been printed:")
for element in completed_models:
	print(f"\t• {element}")