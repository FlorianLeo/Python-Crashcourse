from wuerfel import Wuerfel
# das wird zusäztlich benötigt
from plotly.graph_objs import Bar, Layout
from plotly import offline

# Von der Klasse Wuerfel eine Instanz wuerfel erzeugen
wuerfel_6 = Wuerfel()

# Würfel werfen
ergebnisse = []
for wurfanzahl in range(1000):
	ergebnis = wuerfel_6.werfen()
	ergebnisse.append(ergebnis)

# Analyse des Zufallsgenerators
haeufigkeiten = []
# Achtung nicht stolpern - +1 wird gebraucht um bis 7 zu gehen damit 6 gezählt wird
# anstatt bis 6 zu gehen und damit bei 5 aufzuhören zu zählen 
for wert in range(1, wuerfel_6.flaechen+1):
	haeufigkeit = ergebnisse.count(wert)
	haeufigkeiten.append(haeufigkeit)

# Visualisierung der Häufigkeiten
# Ausdehnung in X - da plotly direkt mit range nicht umgehen kann
# muss der Umweg über list genommen werden
x_werte = list(range(1, wuerfel_6.flaechen+1))
# Vorbereitung der Daten als Balkendarstellung
# Bar ist eine Klasse von plotly und ermöglicht die Balkendarstellung
# Bar muss in eckige Klammern gesetzt werden
daten = [Bar(x=x_werte, y=haeufigkeiten)]

# Darstellung
meine_darstellung = Layout(title='Häufigkeitsverteilung eines 6-seitigen Würfels - 1000 Würfe.',
					xaxis={'title': 'Flächen des Würfels'},
					yaxis={'title': 'Verteilung Häufigkeiten'})

# Ausgabe - erzeugt eine html-Datei - im Browser öffnen
# offline.plot benötigt als Eingabe ein Dictionarry {}
offline.plot({'data': daten, 'layout': meine_darstellung}, filename='wuerfel_6.html')