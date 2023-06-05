"""
You can almost model anything using classes.
This is a simple class, Car, which represents ANY car.
Naming convention is helpful = Capitalized equals to a class
"""
class Car:
	"""A simple attempt to represent a car."""
	def __init__(self, make, model, year):
		"""
		Initialize attributes to describe a car.
		mandatory parameters are: make, model, year
		default parameters are: odometer_reading=0
		"""
		self.make = make
		self.model = model
		self.year = year
		self.odometerReading = 0

	def getDescriptiveName(self):
		"""Return a neatly formatted descriptive output."""
		output = f"{self.year} {self.make} {self.model}"
		return output.title()

	def readOdometer(self):
		"""Print a statement showing the car´s milage."""
		print(f"This car has {self.odometerReading} miles on it.")

	def updateOdometer(self, newMileage):
		"""
		Set the odometer to the given value by new mileage, and
		make sure noone can set it to smaller value
		"""
		if newMileage >= self.odometerReading:
			self.odometerReading = newMileage
		else:
			print("Gotcha - not cheating here, fuckers")

	def incrementOdometer(self, miles):
		"""Add the given amount to the odometer reading."""
		self.odometerReading += miles