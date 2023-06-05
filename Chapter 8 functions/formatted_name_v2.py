def get_formatted_name(first_name, last_name, middle_name=''):
	"""Return a full name, neatly formatted"""
	"""A optional middle name may be given"""
	"""The order of Parameters is: first_name, last_name, middle_name"""
	#When a function returns something, a variable must be provided to hold it
	if middle_name:
		full_name = f"{first_name} {middle_name} {last_name}"
	else:
		full_name = f"{first_name} {last_name}"
	return full_name.title()

#variante 1 mit Umweg über Variable
somename = get_formatted_name('jimi', 'hendrix')
print(somename)
#variante 2 die Funktion direkt in der Print-Funktion aufrufen
print(get_formatted_name('max', 'koller'))
print(get_formatted_name('john', 'hooker', 'lee'))