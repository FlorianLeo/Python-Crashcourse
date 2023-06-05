from random import choice

canditates = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e')
coincidently = choice(canditates)

counter = 1

while True:
    pulled = choice(canditates)
    if pulled == coincidently:
        print(f"\nWe have a match with {coincidently}!")
        print(f"The while-loop was running {counter} times.")
        break
    else:
        print(f"{pulled} was randomly chosen from the Tuple canditates")
    counter += 1