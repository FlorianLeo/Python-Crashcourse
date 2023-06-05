def city_country(city, country):
	"""Provides neatly formated output"""
	neatly_formated = f"{city}, {country}"
	return neatly_formated.title()

print(city_country('zürich', 'schweiz'))
print(city_country('hamburg', 'deutschland'))
print(city_country('paris', 'frankreich'))