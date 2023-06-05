# importiere aus der Bibliothek matplotlib das Modul pyplot unter dem Alias plt
# Das Modul pyplot enthält eine Menge an Funktionen Charts (Hitlisten) und graphische Darstellungen (Plots)
import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
# sehr beliebte Konvetion: aus dem Modul pyplot, alias plt, holen wir die Funktion subplots()
# 2 Variablen: fig und ax
# fig repräsentiert die ganze Figur oder auch die Kollektion aus Darstellungen die erzeugt werden
# ax repräsentiert 1 einzige Darstellung in einer Figur
plt.style.use('seaborn-paper')
# Mögliche Attribute:
# 'Solarize_Light2', '_classic_test_patch', '_mpl-gallery', '_mpl-gallery-nogrid', 'bmh',
# 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn',
# 'seaborn-bright', 'seaborn-colorblind', 'seaborn-dark', 'seaborn-dark-palette', 'seaborn-darkgrid',
# 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook', 'seaborn-paper', 'seaborn-pastel',
# 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'tableau-colorblind10'
fig, ax = plt.subplots()
# auf ax wird die plot Methode angewand der wiederrum die Liste squares übergeben wird
# plot versucht eine graphische Darstellung der ihr übergebenen Liste
# erweitert um die Anweisung die Strichstärke auf 3 zu stellen
#          hier x      hier y
ax.plot(input_values, squares, linewidth=3)

# Beschriftungen (Labels) aendern
ax.set_title("Titel of this Plot", fontsize=24)
ax.set_xlabel("Value for X-axis", fontsize=14)
ax.set_ylabel("Square of Value on Y-axis", fontsize=16)
# TICK-grösse ändern = ist die Textgröße entlang der Markierungen von x und y Achsen
ax.tick_params(axis='both', labelsize=8)

# die Funktion show aus dem Modul pyplot, alias plt, öffnet den Viewer aus Matplotlib um
# die Darstelllung auf den Bildschirm zu bringen
plt.show()