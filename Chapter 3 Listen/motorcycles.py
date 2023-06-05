#Beispiel aus dem Buch
motorcycles = ['honda', 'yamaha', 'suzuki']
print("Liste zum Zeitpunkt der Erstellung")
print(motorcycles)

#hond wird ersetzt durch ducati
print("\nObjekt 0, also honda, wird ersetzt durch ducati")
motorcycles[0] = 'ducati'
print(motorcycles)

#hinzufügen eines objektes
print("\njetzt fügen wir ein objekt ans Ende hinzu durch die methode append")
motorcycles[0] = 'honda'
motorcycles.append('ducati')
print(motorcycles)

#einfügen an einer bestimmten Stelle
print("\njetzt soll an einer bestimmten Stelle eingefügt werden - an die 2. Stelle - vectrix - durch die insert methode")
motorcycles.insert(1, 'vectrix')
print(motorcycles)
print("und wie man sieht klappt es")
print("fügen wir ein weiteres Objekt hinzu - an die 4. Stelle - moto guzzi")
motorcycles.insert(3, 'moto guzzi')
print(motorcycles)

#entfernen eines Objektes
print("\nein bestimmtes Objekt der List soll entfernt werden - yamaha - mit del Statement (nicht Methode!) - das 0, 1, 2. Objekt der Liste!")
print("doch vorsicht - mit del Statement muss der Index bekannt sein!")
del motorcycles[2]
print(motorcycles)

#entfernen mit pop-methode
print("\ngelegentlich wird ein entferntes Objekt noch benötigt - die pop-methode enternt das letzte Objekt einer Liste")
print(motorcycles)
print("Das letzte Objekt wird entfernt und dabei in einer neuen Variablen gespeichert")
popped_motorcycles = motorcycles.pop()
print("hier die liste nach dem pop")
print(motorcycles)
print(f"und hier das entfernte Objekt {popped_motorcycles}")
print("\npop kann auch ein bestimmtes Objekt entfernen - also irgendwo mitten drin - moto guzzi")
print("doch vorsicht - der Index muss bekannt sein!")
next_popped_motorcycle = motorcycles.pop(2)
print(f"die marke {next_popped_motorcycle} wurde entfernt")
print(motorcycles)
print("\nund was wenn die position nicht bekannt ist? richtig - per 'Wert' aufrufen")
print("aber mit der remove-methode - pop ist für Index, remove für 'nach Wert'")
electric_motorcycle = 'vectrix'
motorcycles.remove(electric_motorcycle)
print("was ist übrig?")
print(motorcycles)
print(f"das elektrische Motorrad '{electric_motorcycle}' wurde aus der Liste entfernt")