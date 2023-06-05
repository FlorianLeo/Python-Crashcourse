favorite_languages = {
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
	}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")


print("\nNow lets interate through the whloe dictionary")
for key, value in favorite_languages.items():
	person = key.title()
	language = value.title()
	print(f"The favorite language of {person} is {language}.")


print("\nMit etwas schlankerem Code das gleiche Ergebnis erziehlen")
for every_single_key, every_single_value in favorite_languages.items():
	print(f"{every_single_key.title()}'s favorite language is {every_single_value.title()}.")


print("\nDiesmal nur die Keys aus dem Dictionary anzeigen")
for every_single_key in favorite_languages.keys():
	print(f"{every_single_key.title()}")

print("\nDiesmal nur die Keys aus dem Dictionary anzeigen")
for every_single_key in favorite_languages:
	print(f"{every_single_key.title()}")	

print("\nDiesmal nur die Keys aus dem Dictionary anzeigen")
for every_single_value in favorite_languages.values():
	print(f"{every_single_value.title()}")


