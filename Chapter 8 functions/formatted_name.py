def get_formatted_name(first_name, last_name):
	"""Return a full name, neatly formatted"""
	#When a function returns something, a variable must be provided to hold it
	full_name = f"{first_name} {last_name}"
	return full_name.title()

#variante 1
somename = get_formatted_name('jimi', 'hendrix')
print(somename)
#variante 2
print(get_formatted_name('max', 'koller'))