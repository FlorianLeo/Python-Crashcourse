from random import randint

class Wuerfel:
	"""Eine Klasse um Würfel zu repräsentieren"""

	def __init__(self, flaechen=6):
		"""Es wir ein normaler Würfel mit 6 Flächen genommen."""
		# W6 = Würfel mit 6 Flächen
		# W8 = Würfel mit 8 Flächen
		self.flaechen = flaechen

	def werfen(self):
		"""Würfel werfen = Zufallswert von 1-6 erzeugen"""
		# randint verwenden um eine Zahl zwischen 1 und der Würfelflächenanzahl zu erzeugen
		return randint(1, self.flaechen)