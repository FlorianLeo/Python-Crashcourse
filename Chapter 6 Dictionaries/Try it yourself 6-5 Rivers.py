rivers ={
	'nil':'egypt',
	'limmat':'switzerland',
	'donau':'europe',
	'thur':'switzerland'
}
# Durch das Dict Loopen und eine Satz aus Keys und Values erzeugen
print('Aus dem Dictionary, den Keys und Values, eine Satz bauen.')
for single_key, single_value in rivers.items():
	print(f"The {single_key.title()} runs through {single_value.title()}.")
	
# Durch das Dict Loopen und NUR die Keys anzeigen
# Variante "plump"
print('\nNur die Keys anzeigen - Methode 1 zum Loopen.')
for single_key in rivers.keys():
	print(single_key.title())
# Variante "schlank" - per default itteriert eine FOR durch die Keys
print('\nNur die Keys anzeigen - Methode 2 zum Loopen.')
for single_key in rivers:
	print(single_key.title())

# Durch das Dict Loopen und NUR die Values anzeigen
print('\nNur die Values anzeigen.')
for single_value in rivers.values():
	print(single_value.title())