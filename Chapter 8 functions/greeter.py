#Beispiel Definition einer Funktion
#das value_passed_to_fuction nennt man Parameter
def greet_user(value_passed_to_function):
	#Tripple Anführungszeichen bedeutet im Body einer Funktion "docstring"
	"""Display a simple greeting."""
	print(f"Hello, {value_passed_to_function.title()}!")

#Wir die Funktion aufgerufen ist das in den runden Klammern das Argument das an die Funktion übergeben wird
greet_user('jessica')