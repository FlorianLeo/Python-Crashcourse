favorite_languages = {
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
	}
names = ['edward', 'urs', 'jan', 'jen', 'holger', 'hesam', 'sarah', 'phil']

print('Variante mit einem Zwischenschritt')
for single_name in names:
	same_name = single_name
	if same_name in favorite_languages:
		print(f'Thank you {same_name.title()} for taking the poll.')
	else:
		print(f'Hey {same_name.title()} - WTF are you participating in the poll?!')

print('\nVariante ohne Zwischenschritt')
for element in names:
	if element in favorite_languages:
		print(f'Thank you {element.title()} for taking the poll.')
	else:
		print(f'Hey {element.title()} - WTF are you participating in the poll?!')