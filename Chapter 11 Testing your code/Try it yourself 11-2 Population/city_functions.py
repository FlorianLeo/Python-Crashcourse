def get_formated_string(city, country, population=''):
	"""Return neatly formated String of a city and its country"""
	if population:
		nice_string = f"{city}, {country} - population of {population}"
	else:
		nice_string = f"{city}, {country}"
	return nice_string.title()