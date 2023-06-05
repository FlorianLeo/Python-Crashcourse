
# You can almost model anything using classes.
# This is a simple class, Dog, which represents a dog - not 1 dog, but ANY dog.
# Naming convention is helpful = Capitalized equals to a class
class Dog:
	"""A Simple attempt to model a dog."""
	# A Function that is part of a class is called a method = every def UNDER the class Dog is a method
	# We define the __init__() method to have thre parameters: self, name and age.
	# The self parameter is mandatory in the method definition, and it MUST COME FIRST before the other parameters
	def __init__(self, name, age):
		"""Initialize name and age attributes."""
		# The two variables defined here have the prefix self.
		# Any variable prefixed with self is available to every other method
		# in the class, like the two here, sit and rollover,
		# and we will also be able to access these variable through
		# an instance created from the class.
		self.name = name
		self.age = age

	def sit(self):
		"""Simulate a dog sittin gin response to a command."""
		print(f"{self.name} is now sitting.")

	def roll_over(self):
		"""Simulate rolling over in response to a command."""
		print(f"{self.name} rolled over!")

# Making 2 instance from a class Dog, my_dog and your_dog
# Think of a class as set of instructions what the object has to look like
# You need to know ALL the attributes
# You either know the EXACT order of attributes, or name them 
my_dog = Dog('Willi', 6)
your_dog = Dog(age=3, name='Lucy')

# Accessing the Attributes is as simple as that, using the dot-notation.
# Of course, you have to know the attribute´s name
# as defined in the Class (def __init__(self, name, age)).
print(f"My dog´s name is {my_dog.name}, and it is {my_dog.age} years old.")
print(f"Your dog´s name is {your_dog.name}. and it is {your_dog.age} years old.")

# Calling the other 2 methods from withing this class
# again using the dot-notation = call the instance (my_dog, your_dog) followed by
# .sit() or by .rollover()
my_dog.sit()
your_dog.sit()
my_dog.roll_over()
your_dog.roll_over()