from wuerfel import Wuerfel

# Von der Klasse Wuerfel eine Instanz wuerfel erzeugen
wuerfel_d6 = Wuerfel()


# Würfel werfen
ergebnisse = []
for wurfanzahl in range(1000):
	ergebnis = wuerfel_d6.werfen()
	ergebnisse.append(ergebnis)

# Analyse des Zufallsgenerators
haeufigkeiten = []
# Achtung nicht stolpern - +1 wird gebraucht um bis 7 zu gehen damit 6 gezählt wird
# anstatt bis 6 zu gehen und damit bei 5 aufzuhören zu zählen 
for wert in range(1, wuerfel_d6.flaechen+1):
	haeufigkeit = ergebnisse.count(wert)
	haeufigkeiten.append(haeufigkeit)

print(ergebnisse)
print(haeufigkeiten)