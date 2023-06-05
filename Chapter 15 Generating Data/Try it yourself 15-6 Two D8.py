from wuerfel import Wuerfel
# das wird zusäztlich benötigt
from plotly.graph_objs import Bar, Layout
from plotly import offline

# Von der Klasse Wuerfel eine Instanz wuerfel erzeugen
wuerfel_8_1 = Wuerfel(8)
wuerfel_8_2 = Wuerfel(8)

# Würfel werfen
ergebnisse = []
for wurfanzahl in range(50000):
	ergebnis = wuerfel_8_1.werfen() + wuerfel_8_2.werfen()
	ergebnisse.append(ergebnis)

# Analyse des Zufallsgenerators
haeufigkeiten = []
# Achtung nicht stolpern - +1 wird gebraucht um bis 13 zu gehen damit 12 gezählt wird
# anstatt bis 12 zu gehen und damit bei 11 aufzuhören zu zählen
summe_flaechen = wuerfel_8_1.flaechen+wuerfel_8_2.flaechen
for wert in range(2, summe_flaechen+1):
	haeufigkeit = ergebnisse.count(wert)
	haeufigkeiten.append(haeufigkeit)

# Visualisierung der Häufigkeiten
# Ausdehnung in X - da plotly direkt mit range nicht umgehen kann
# muss der Umweg über list genommen werden
x_werte = list(range(2, summe_flaechen+1))
# Vorbereitung der Daten als Balkendarstellung
# Bar ist eine Klasse von plotly und ermöglicht die Balkendarstellung
# Bar muss in eckige Klammern gesetzt werden
daten = [Bar(x=x_werte, y=haeufigkeiten)]

# Darstellung
meine_darstellung = Layout(title='Häufigkeitsverteilung 2 8-seitige Würfel - 50000 Würfe.',
					xaxis={'title': 'Summe der Werte der Würfelflächen', 'dtick': 1},
					yaxis={'title': 'Verteilung Häufigkeiten'})

# Ausgabe - erzeugt eine html-Datei - im Browser öffnen
# offline.plot benötigt als Eingabe ein Dictionarry {}
offline.plot({'data': daten, 'layout': meine_darstellung}, filename='Tiy15-6.html')