#Passing Arguments - PLURAL!
#Positional Arguments: must be passed in the same order as defined in the function
#Function is defined with 2 Parameters
def describe_pet(pet_type, pet_name):
	"""Display the kind of animal, and its name"""
	"""First Parameter/Argument that must be passed is the type of animal"""
	"""Second Parameter/Argument that must be passed is the name of the animal"""
	print(f"\nI have a {pet_type}.")
	print(f"My {pet_type}´s name is {pet_name.title()}.")
#Now pass the Arguments IN THE ORDER AS IN THE DEFINITION - DON'T MIX THEM UP
describe_pet('hamster', 'harry')
describe_pet('cat', 'sphinx')
describe_pet('dog', 'brutus')

#Keyword Arguments: is a name-value-pair passed to the function
#By doing so the sequence of Arguments is irrelevant.
#The function call explicitly the Arguments to the corresponding Parameter
describe_pet(pet_name='lily', pet_type='bird') 


#Default Values
#it is good habit to provide default values for Parameters
#if the function call contains all Arguments that are in the function definition,
#the passed Arguments override the defaults from the function definition.
#Make shure that the the Parameters that should have a default come last!!
def describe_pet_with_defaults(pet_name, pet_type='dog'):
	"""Display the kind of animal, and its name"""
	"""First Parameter/Argument that must be passed is the type of animal"""
	"""Second Parameter/Argument that must be passed is the name of the animal"""
	print(f"\nI have a {pet_type}.")
	print(f"My {pet_type}´s name is {pet_name.title()}.")

describe_pet_with_defaults('willie')
describe_pet_with_defaults(pet_name='batiatus')
describe_pet_with_defaults('lily', pet_type='bird')
#this doesn't work
#describe_pet_with_defaults(pet_type='bird', 'lily')
describe_pet_with_defaults(pet_type='bird', pet_name='lily')