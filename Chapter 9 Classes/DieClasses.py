from random import randint
"""
You can almost model anything using classes.
This is a simple class, Die, which represents ANY Die.
Naming convention is helpful = Capitalized equals to a class
"""
class Die:
	"""A simple attempt to represent a Die"""
	def __init__(self):
		"""Initialize a 6 sided Die"""
		self.sides = 6

	def rollDie(self):
		"""Roll the Die and return a random number"""
		if self.sides == 6:
			counter = 0
			print(f"It is a {self.sides} sided Die - lets roll it 10 times")
			while counter < 10:
				dieValue = randint(1, 6)
				print(f"The Die rolled to: {dieValue}")
				counter += 1
		elif self.sides == 10 or self.sides == 20:
			counter = 0
			print(f"It is a {self.sides} sided Die - lets roll it 10 times")
			if self.sides == 10:
				while counter < 10:
					dieValue = randint(1, 10)
					print(f"The Die rolled to: {dieValue}")
					counter += 1
			else:
				while counter < 10:
					dieValue = randint(1, 20)
					print(f"The Die rolled to: {dieValue}")
					counter += 1