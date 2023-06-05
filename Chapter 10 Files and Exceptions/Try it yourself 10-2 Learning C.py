filename = 'learning_python.txt'
content = []

# Den Inhalt der Datei in einer Variablen zwischenspeichern und dann bearbeiten
with open(filename) as file_object:
	content = file_object.readlines()

for element in content:
	print(element.strip().replace('Python', 'C'))

