#In this example, range() prints only the numbers 1 through 4
#This is an example of the off-by-one behavior
#The range function causes Python to start counting at the first value you give it,
#and it stops when it reaches the second value you provide.
#Because it stops at the second value, the output never contains the end value,
#which would have been 5 in this case.
#so to make it work replace 5 with 6
for value in range(1, 5):
	print(value)

print(f"repeat the loop different")

for value in range(1, 6):
	print(value)

print(f"another example")

numbers = list(range(1, 6))
print(numbers)