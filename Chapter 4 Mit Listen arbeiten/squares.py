#liefere das Quadrat der Zahlen von 1-10
quadratzahlen = []
for value in range(1, 11):
	quadrat = value ** 2
	quadratzahlen.append(quadrat)
print(quadratzahlen)

print(f"\nNow the same example more conconcisely in the code")

#create empty list
quadratzahlen = []
#use for together with range to create numbers 1-10
for value in range(1, 11):
	#fill the list immediately with the result from range to the power of 2
	quadratzahlen.append(value ** 2)
print(quadratzahlen)

print(f"\nAnd now in code the version with list comprehension")
#instead of having 4 lines you just need 2
quadratzahlen = [value ** 2 for value in range(1, 11)]
print(quadratzahlen)