import unittest
from city_functions import get_formated_string

class CitiesNamesTest(unittest.TestCase):
	"""Test function 'get_formated_string()' if it works"""
	# make shure the function's starts with test_
	def test_city_country(self):
		nice_string = get_formated_string('zürich', 'schweiz')
		self.assertEqual(nice_string, 'Zürich, Schweiz')

if __name__ == '__main__':
	unittest.main()