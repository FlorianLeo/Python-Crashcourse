# Liste der vorhandenen Benutzer
current_users = ['admin', 'john', 'marry', 'james', 'lydia']
# Kopie der Liste vorhandener Benutzer mit großem Anfangsbuchstaben, nutze aus Kapitel 4 die List Comprehensions
current_users_capitalized = [element.title() for element in current_users.copy()]
# Kopie der Liste vorhandener Benutzer alle Buchstaben großgeschrieben, nutze aus Kapitel 4 die List Comprehensions
current_users_upper = [element.upper() for element in current_users.copy()]
# Falls nötig die erzeugten Listen anzeigen lassen
#print(current_users)
#print(current_users_capitalized)
#print(current_users_upper)
# Liste der neuen Benutzer
new_users = ['carl', 'james', 'florian', 'urs', 'marry']
# Falls nötich die Liste der neuen Benutzer anzeigen lassen
#print(new_users)
for element in new_users:
	if element in current_users:
		print(f'\nSorry {element}, the username you have chosen is already in use.')
		print('Please, use a different name.')
	elif element in current_users_capitalized:
		print(f'\nSorry {element}, the username you have chosen is already in use.')
		print('Please, use a different name.')
	elif element in current_users_upper:
		print(f'\nSorry {element}, the username you have chosen is already in use.')
		print('Please, use a different name.')
	else:
		print(f'\nHello {element}, and welcome to the world')