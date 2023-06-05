from carClasses import Car
from BatteryClasses import Battery75
"""
You can almost model anything using classes.
This is a simple class, Car, which represents ANY car.
Naming convention is helpful = Capitalized equals to a class
"""
# Vererbung: die Klasse ist ein Child vom Parent Car. Siehe (Car)
class ElectricCar(Car):
	"""The parent class is Car, and here are specialities for electric cars only"""
	def __init__(self, make, model, year):
		"""
		Initialize attributes of the parent class.
		Followed by specifics to an electric car.
		"""
		super().__init__(make, model, year)
		# Instance as Attribute!! Be careful here and later when calling it.
		# This line creates an Object from the class Battery75.
		# self.battery is filled with an instanciation of class Battery75
		self.energyStorage = Battery75()