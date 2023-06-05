def build_person(first_name, last_name, age=None):
	"""Returns a Dictionary with the Arguments passed to the function"""
	"""Required in order is: first_name, last_name"""
	"""And OPTIONAL on the 3rd positon the age"""
	person = {'first':first_name, 'last':last_name}
	if age:
		person['age'] = age
	return person
someone = build_person('jimi', 'hendrix', 27)
print(someone)
someone = build_person('marc', 'anthony', age=57)
print(someone)