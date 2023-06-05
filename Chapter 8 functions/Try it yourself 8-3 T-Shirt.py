def make_shirt(shirt_size, shirt_txt):
	"""the function Parameters are:"""
	"""shirt_size - which asks for the Size"""
	"""shirt_txt - asks for the text to printed on the shirt"""
	print(f"\nThe size is: {shirt_size}")
	print(f"And its text is: '{shirt_txt}'")
#call the function with positional arguments - sequence does matter
make_shirt(42, 'Turn on, tune in, and drop out')
#call the function with keyword arguments - sequence does not matter
make_shirt(shirt_txt='Turn on, tune in, and drop out', shirt_size=24)