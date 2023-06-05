filename = 'pi_million_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()
pi_string = ''
for element in lines:
	pi_string += element.strip()

print(f"{pi_string[:52]}...")