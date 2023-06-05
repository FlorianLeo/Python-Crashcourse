human_1 = {
		'first_name':'urs',
		'last_name':'baumann',
		'age':45,
		'city':'zürich'
}
human_2 = {
		'first_name':'jan',
		'last_name':'vandromme',
		'age':40,
		'city':'windisch'
}
human_3 = {
		'first_name':'pascal',
		'last_name':'bücheler',
		'age':29,
		'city':'zürich'
}
humans = [human_1, human_2, human_3]
for element in humans:
	print('Eintrag:')
	for key, value in element.items():
		if key == 'first_name':
			print(f"\tVorname: {value.title()}")
		elif key == 'last_name':
			print(f"\tNachname: {value.title()}")
		elif key == 'age':
			print(f"\tAlter: {value}")
		elif key == 'city':
			print(f"\tWohnort: {value.title()}")