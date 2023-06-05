"""
You can almost model anything using classes.
This is a simple class, Car, which represents ANY car.
Naming convention is helpful = Capitalized equals to a class
"""
class Battery75:
	"""A simple attempt to modell a 75kWh Battery."""
	def __init__(self):
		"""Initialize the Energy contained in the battery."""
		self.kiloWattHour = 75
		self.weight = 1_200
	def describeBattery(self):
		"""Print statement describing the battery."""
		print(f"The battery stores nominal {self.kiloWattHour}kWh of electric energy.")
		print(f"The battery has a weight of {self.weight}kg.")
	def getMilageEstimate(self):
		"""Print statement describing the estimated range according to the car"""
		if self.kiloWattHour == 75:
			estimatedMilage = 260
		else:
			estimatedMilage = 300
		print(f"This car will drive about {estimatedMilage} miles on a full charge.")