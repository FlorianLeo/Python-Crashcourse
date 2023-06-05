#der 3. Parameter, der Name muss später in der Funktion als Name für das
#Dictionary verwendet werden.
#der Doppel-Asterisk stösst die Erzeugung eines Dicts an
def build_profile(first, last, **user_params):
	"""Build a dictionary containing everything we know"""
	user_params['first_name'] = first
	user_params['last_name'] = last
	return user_params

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')

print(user_profile)