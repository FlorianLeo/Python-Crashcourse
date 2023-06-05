from wuerfel import Wuerfel
# das wird zusäztlich benötigt
from plotly.graph_objs import Bar, Layout
from plotly import offline

# Von der Klasse Wuerfel eine Instanz wuerfel erzeugen
wuerfel_6_1 = Wuerfel()
wuerfel_6_2 = Wuerfel()
summe_flaechen = wuerfel_6_1.flaechen*wuerfel_6_2.flaechen

# Würfel werfen mit List-Comprehension erstellen
# Um es besser zu verstehen liest man es von rechts nach links
ergebnisse = [wuerfel_6_1.werfen() * wuerfel_6_2.werfen() for wurfanzahl in range(500000)]

# Analyse des Zufallsgenerators mit List-Comprehension erstellen
# Achtung nicht stolpern - +1 wird gebraucht um bis 37 zu gehen damit 36 gezählt wird
# anstatt bis 36 zu gehen und damit bei 35 aufzuhören zu zählen
# Um es besser zu verstehen liest man es von rechts nach links
haeufigkeiten = [ergebnisse.count(wert) for wert in range(1, summe_flaechen+1)]

# Visualisierung der Häufigkeiten
# Ausdehnung in X - da plotly direkt mit range nicht umgehen kann
# muss der Umweg über list genommen werden
x_werte = list(range(1, summe_flaechen+1))
# Vorbereitung der Daten als Balkendarstellung
# Bar ist eine Klasse von plotly und ermöglicht die Balkendarstellung
# Bar muss in eckige Klammern gesetzt werden
daten = [Bar(x=x_werte, y=haeufigkeiten)]

# Darstellung
meine_darstellung = Layout(title='Häufigkeitsverteilung Multiplikation 2 6-seitiger Würfel - 500000 Würfe.',
					xaxis={'title': 'Summe der Werte der Würfelflächen', 'dtick': 1},
					yaxis={'title': 'Verteilung Häufigkeiten'})

# Ausgabe - erzeugt eine html-Datei - im Browser öffnen
# offline.plot benötigt als Eingabe ein Dictionarry {}
offline.plot({'data': daten, 'layout': meine_darstellung}, filename='Tiy15-9.html')