# You can almost model anything using classes.
# This is a simple class, Restaurant, which represents ANY restaurant.
# Naming convention is helpful = Capitalized equals to a class
class Restaurant:
	"""A Simple attempt to model a restaurant."""
	# A Function that is part of a class is called a method = every def UNDER the class Restaurant is a method
	# We define the __init__() method to have thre parameters: self, restaurant_type and cuisine_type.
	# The self parameter is mandatory in the method definition, and it MUST COME FIRST before the other parameters
	def __init__(self, restaurant_type, cuisine_type):
		self.rest_type = restaurant_type
		self.cuis_type = cuisine_type
		self.number_served = 0

	def decribe_restaurant(self):
		print(f"The Restaurant is of Type: {self.rest_type}.")
		print(f"The Cuisine can be called: {self.cuis_type}.")

	def open_restaurant(self):
		print("The Restaurant is currently opened.")

	def set_number_served(self, new_number):
		self.number_served = new_number

	def increment_number_served(self, increment_by):
		self.number_served += increment_by

rathauskeller = Restaurant(cuisine_type='gut bürgerlich', restaurant_type='Schweizer Traditionshaus')
rathauskeller.decribe_restaurant()
rathauskeller.open_restaurant()

print(rathauskeller.number_served)
rathauskeller.number_served = 10
print(rathauskeller.number_served)
rathauskeller.set_number_served(20)
print(rathauskeller.number_served)
rathauskeller.increment_number_served(100)
print(rathauskeller.number_served)