favorite_languages = {
	'jen':['python', 'ruby'],
	'sarah':['c'],
	'edward':['ruby', 'go'],
	'phil':['python', 'haskell']
	}

for key, value in favorite_languages.items():
	if len(value) > 1:
		print(f'\n{key.title()}´s favorite languages are:')
		for element in value:
			print(f'\t{element.title()}')
	else:
		print(f'\n{key.title()}´s favorite language is:')
		for element in value:
			print(f'\t{element.title()}')