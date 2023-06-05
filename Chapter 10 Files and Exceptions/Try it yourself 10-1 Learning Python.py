filename = 'learning_python.txt'

# Den Inhalt der Datei einfach anzeigen
with open(filename) as file_object:
	inhalt = file_object.readlines()
	print(inhalt)
# Den Inhalt der Datei Zeile für Zeile anzeigen
with open(filename) as file_object:
	for zeile in file_object:
		print(zeile)
# Den Inhalt der Datei in einer Variablen zwischenspeichern und dann bearbeiten
with open(filename) as file_object:
	content = file_object.readlines()

for element in content:
	print(element.strip())