from random import choice
from itertools import repeat

canditates = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e')

for i in range(0, 5):
 print(f"The Candiate {choice(canditates)} wins a ticket")