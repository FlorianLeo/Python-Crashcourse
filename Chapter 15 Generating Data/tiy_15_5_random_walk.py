from random import choice
#from time import sleep

class RandomWalk:
	"""A class to generat random walks."""

	def __init__(self, num_points=5000):
		"""Inititalize attributes of a walk."""
		self.num_points = num_points

		# All walks start at (0, 0).
		self.x_values = [0]
		self.y_values = [0]

	def fill_walk(self):
		"""Create all points in the walk."""

		# Keep taking steps until the walk reaches the desired length.
		while len(self.x_values) < self.num_points:

			x_step=self.get_step()
			y_step=self.get_step()

			#Reject moves that go nowhere.
			if x_step == 0 and y_step == 0:
				continue

			# Calculate the new position.
			x_neu = self.x_values[-1] + x_step
			y_neu = self.y_values[-1] + y_step

			self.x_values.append(x_neu)
			self.y_values.append(y_neu)

	def get_step(self):
		"""Calculate a single step"""
		
		direction = choice([1, -1])
		distance = choice(range(5))
		step = distance * direction
		return step