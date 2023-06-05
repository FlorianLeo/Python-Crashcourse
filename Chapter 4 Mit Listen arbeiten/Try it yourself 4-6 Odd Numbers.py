#Working "regularly"
odd_numbers = list(range(1, 21, 2))
for element in odd_numbers:
	print(element)

#Working with list comprehension
odd_numbers = [element for element in list(range(1, 21, 2))]
for element in odd_numbers:
	print(element)