print("Slicing a List")
print("To make a slice, you specify the index of the first and last elements you want to work with.")
print("As with the range() function, Pyhton stops one item before the second index you specify.")
print("To output the first thre elements in a list, you would request indices 0 through 3,")
print("which would return elements 0, 1, and 2.")
print("'charls', 'martina', 'michael', 'florence', 'eli'\n")

players = ['charls', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

print("\nyou can generat any subset of a list. For example, if you want the second, third, and fourth")
print("items in a list, you would start the slice at index 1 and end at index 4\n")

players = ['charls', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])

print("\nIf you omit the first index in a slice, Python automatically starts your slice at the beginning of the list\n")

players = ['charls', 'martina', 'michael', 'florence', 'eli']
print(players[:4])

print("\nA similar syntax works if you wnat a slcie that includes the end of a list\n")

players = ['charls', 'martina', 'michael', 'florence', 'eli']
print(players[2:])

print("\nRecall that a negative index returns an element a certain distance from the end of a list;")
print("therefore, you can output any slice from the end of a list\n")

players = ['charls', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])

print("\nUse a for loop to loop through a slice\n")

players = ['charls', 'martina', 'michael', 'florence', 'eli']
print("here are the first three players on my team:")
for player in players[:3]:
	print(player.title())