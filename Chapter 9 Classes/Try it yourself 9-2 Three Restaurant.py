# You can almost model anything using classes.
# This is a simple class, Restaurant, which represents ANY restaurant.
# Naming convention is helpful = Capitalized equals to a class
class Restaurant:
	"""A Simple attempt to model a restaurant."""
	# A Function that is part of a class is called a method = every def UNDER the class Restaurant is a method
	# We define the __init__() method to have thre parameters: self, restaurant_type and cuisine_type.
	# The self parameter is mandatory in the method definition, and it MUST COME FIRST before the other parameters
	def __init__(self, restaurant_type, cuisine_type):
		"""Initialize the restaurant_type followed by cuisine_type"""
		self.rest_type = restaurant_type
		self.cuis_type = cuisine_type

	def decribe_restaurant(self):
		"""Print the attributes of the restaurant"""
		print(f"\nThe Restaurant is of Type: {self.rest_type}.")
		print(f"The Cuisine can be called: {self.cuis_type}.")

	def open_restaurant(self):
		"""Say that the Restaurant is open"""
		print("The Restaurant is currently opened.")

rathauskeller = Restaurant(cuisine_type='gut bürgerlich', restaurant_type='Schweizer Traditionshaus')
brasserie_freilager = Restaurant('International', 'a la carte')
pasta_station = Restaurant('Take away', 'italienische Küche')

rathauskeller.decribe_restaurant()
brasserie_freilager.decribe_restaurant()
pasta_station.decribe_restaurant()