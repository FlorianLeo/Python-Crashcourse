#arbeiten mit Listen
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print("Nicht ganz was Benutzer sehen sollten - wir manipulieren etwas")
print("Listen sind eine geordnete Ansammlung von Objekten")
print("Zeigen wir das 1. Objekt - also Objekt 0")
print(bicycles[0])
print("Zeigen wir das 2. Objekt - also Objekt 1")
print(bicycles[1])
print("Zeigen wir das 3. Objekt - also Objekt 2")
print(bicycles[2])
print("Zeigen wir das 4. Objekt - also Objekt 3")
print(bicycles[3])
print("Und jetzt noch den Anfangsbuchstaben gross")
print(bicycles[0].title())
print("Python hat eine spezielle Methode um das letzte Element einer Liste aufzurufen: mit -1")
print(bicycles[-1])
print("Und jetzt noch den Anfangsbuchstaben gross")
print(bicycles[-1].title())
print("Die spezielle Methode ist erweiterbar um z.B. das vorletzte Element einer Liste aufzurufen: mit -2")
print(bicycles[-2].title())
print("das geht so weiter - einfach den negativen Wert erhöhen")
print("Die Objekte einer Liste lassen sich auch für f-Strings verwenden")
message = f"Mein erstes Velo war ein {bicycles[0].title()}"
print(message)
message = f"Mein zweites Velo war ein {bicycles[1].title()}"
print(message)
message = f"Mein drittes Velo war ein {bicycles[2].title()}"
print(message)
message = f"Mein viertes Velo war ein {bicycles[3].title()}"
print(message)