# You can almost model anything using classes.
# This is a simple class, User, which represents ANY user.
# Naming convention is helpful = Capitalized equals to a class
class User:
	"""A Simple attempt to model a user."""
	# A Function that is part of a class is called a method = every def UNDER the class User is a method
	# We define the __init__() method to have thre parameters: self, user_type and cuisine_type.
	# The self parameter is mandatory in the method definition, and it MUST COME FIRST before the other parameters
	def __init__(self, surname, name, age, place_of_birth, day_of_birth, month_of_birth, year_of_birth):
		"""Initialize the user_type followed by cuisine_type"""
		self.user_firstname = surname
		self.user_lastname = name
		self.user_age = age
		self.user_placeofbirth = place_of_birth
		self.user_dayofbirth = day_of_birth
		self.user_monthofbirth = month_of_birth
		self.user_yearofbirth = year_of_birth
		self.login_attempts = 0

	def decribe_user(self):
		"""Print the attributes of the user"""
		print(f"\nThe User´s Name is:\t\t\t\t{self.user_lastname.title()}")
		print(f"The User´s Surname is:\t\t\t{self.user_firstname.title()}")
		print(f"The User was born at:\t\t\t{self.user_placeofbirth.title()}")
		print(f"The User was born in (d-m-y):\t{self.user_dayofbirth}-{self.user_monthofbirth}-{self.user_yearofbirth}")
		print(f"The User is of age:\t\t\t\t{self.user_age}")

	def greet_user(self):
		"""Print a simple greeting to the user"""
		print(f"\nHello {self.user_firstname.title()} {self.user_lastname.title()}. You are welcome!")

	def increment_login_attempts(self):
		"""Increment the Attribute by 1"""
		self.login_attempts += 1

	def reset_login_attempts(self):
		"""Set the attempts to zero"""
		self.login_attempts = 0

florian = User('florian', 'cokl', 50, 'innsbruck', 16, 10, 1971)
astrid = User(name='deutsch', surname='astrid', age=51, place_of_birth='frauenfeld', year_of_birth=1970, month_of_birth=1, day_of_birth=31)

florian.decribe_user()
florian.greet_user()
astrid.decribe_user()
astrid.greet_user()
counter = 0
while counter < 3:
	print(f"\nThis is the {counter + 1}. While-loop´s run")
	print(f"The login attempt counter = {florian.login_attempts}")
	if counter < 2:
		print("Incrementing login attempt counter")
	florian.increment_login_attempts()
	counter += 1

print("\nSetting the login attempt counter back to 0")
florian.reset_login_attempts()
print(florian.login_attempts)