def describe_city(city_name, city_country='Iceland'):
	"""the function Parameters are:"""
	"""city_name - which asks for the name of the city"""
	"""city_country - asks for the country the city is in"""
	print(f"\n{city_name.title()} is in {city_country.title()}")

describe_city('reykjavik')
describe_city('amsterdam')
describe_city('amsterdam', 'netherlands')
describe_city(city_name='wien', city_country='österreich')
describe_city(city_country='switzerland', city_name='winterthur')