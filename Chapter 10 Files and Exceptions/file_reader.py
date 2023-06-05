filename = 'pi_digits.txt'

with open('pi_digits.txt') as file_object:
	contents = file_object.read()
print(contents)


with open('pi_digits.txt') as file_object:
	for line in file_object:
		print(line.rstrip())

with open(filename) as file_object:
	lines = file_object.readlines()
	print(lines)
for line in lines:
	print(line.rstrip())