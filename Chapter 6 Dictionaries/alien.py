"""
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for element in aliens:
	print(element)
"""
aliens = []
for number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed':'slow'}
	aliens.append(new_alien)

#print(aliens)

for element in aliens[:5]:
	print(element)
print('...')
print(f'Total number of aliens: {len(aliens)}')

for element in aliens[:3]:
	if element['color'] == 'green':
		element['color'] = 'yellow'
		element['speed'] = 'medium'
		element['points'] = 10

for element in aliens[:5]:
	print(element)
print('...')
print(f'Total number of aliens: {len(aliens)}')
