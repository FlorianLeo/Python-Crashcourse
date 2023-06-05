# You can almost model anything using classes.
# This is a simple class, Car, which represents ANY car.
# Naming convention is helpful = Capitalized equals to a class
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
		self.odometer_reading = 0
	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive output."""
		output = f"{self.year} {self.make} {self.model}"
		return output.title()
	def read_odometer(self):
		"""Print a statement showing the car´s milage."""
		print(f"This car has {self.odometer_reading} miles on it.")
	def update_odometer(self, mileage):
		"""
		Set the odometer to the given value by mileage, and
		make sure noone can set it to smaller value
		"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("Gotcha - not cheating here, fuckers")
	def increment_odometer(self, miles):
		"""Add the given amount to the odometer reading."""
		self.odometer_reading += miles

# Klasse für Batterie erzeugen da die Attribute variieren könnten
class Battery75:
	"""A simple attempt to modell a 75kWh Battery."""
	def __init__(self):
		"""Initialize the Energy contained in the battery."""
		self.kilo_watt_hour = 75
		self.weight = 1_200
	def describe_battery(self):
		"""Print statement describing the battery."""
		print(f"The battery stores nominal {self.kilo_watt_hour}kWh of electric energy.")
		print(f"The battery has a weight of {self.weight}kg.")
	def get_milage_estimate(self):
		"""Print statement describing the estimated range according to the car"""
		if self.kilo_watt_hour == 75:
			estimated_milage = 260
		else:
			estimated_milage = 300
		print(f"This car will drive about {estimated_milage} miles on a full charge.")

# Vererbung: die Klasse ist ein Child vom Parent Car. Siehe (Car)
class Electric_Car(Car):
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
		self.battery = Battery75()

# Instanz der Unter-Klasse erzeugen, ein Kind von Car, ein Objekt
print("Now an instance from subclass Electric_Car is being created - an Object")
my_tesla = Electric_Car('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
# Achtung auf die Syntax.
my_tesla.battery.describe_battery()
my_tesla.battery.get_milage_estimate()