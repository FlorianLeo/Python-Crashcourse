def make_shirt(shirt_txt='I love Python', shirt_size='large'):
	"""the function Parameters are:"""
	"""shirt_size - which asks for the Size"""
	"""shirt_txt - asks for the text to printed on the shirt"""
	print(f"\nThe size is: {shirt_size}")
	print(f"And its text is: '{shirt_txt.capitalize()}'")
#call the function with positional arguments - sequence does matter
make_shirt('turn on, tune in, and drop out')
#call the function with keyword arguments - sequence does not matter
make_shirt(shirt_txt='turn on, tune in, and drop out', shirt_size='small')
#call the function only
make_shirt()