favorite_numbers = {
	'urs':20,
	'holger':30,
	'hesam':25,
	'jan':584,
	'felix':4562,
	'florian':4711
}
key_missing = 'Leider wurde für diesen Menschen kein Wert hinterlegt'
print(favorite_numbers)
print(f'Die Lieblingszahl von Urs ist: {favorite_numbers.get("urs")}')
print(f"Die Lieblingszahl von Holger ist: {favorite_numbers.get('holger')}")
print(f"Die Lieblingszahl von Hesam ist: {favorite_numbers['hesam']}")
print(f"Die Lieblingszahl von Jan ist: {favorite_numbers['jan']}")
print(f"Die Lieblingszahl von Felix ist: {favorite_numbers['felix']}")
print(f"Die Lieblingszahl von Florian ist: {favorite_numbers['florian']}")
print(f"Die Lieblingszahl von Heidi ist: {favorite_numbers.get('heidi', key_missing)}")
print(f"Die Lieblingszahl von Yolanda ist: {favorite_numbers.get('yolanda', 'Leider hat Yolanda keine Lieblingszahl')}")