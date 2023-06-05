import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Begin a random walk.
while True:
	# rw ist die Instanz der Klasse RandomWalk
	rw = RandomWalk(100)
	# rw führt die Funktion fill_walk aus
	rw.fill_walk()

	# Plot the points in the walk.
	plt.style.use('classic')
	fig, ax = plt.subplots(figsize=(6, 4), dpi=254)
	steps_for_the_walk = range(rw.num_points)

	ax.plot(rw.x_values, rw.y_values, c='black', linewidth=0.25)

	# Achsen und Titel
	ax.set_title("Try it yourslef 15-3 Molecular Motion", fontsize=10)
	ax.set_xlabel("Werte von X", fontsize=5)
	ax.set_ylabel("Werte von Y", fontsize=5)
	ax.tick_params(axis='both', labelsize=3)

	plt.savefig('Tiy15-3.v1.png', bbox_inches='tight')
	plt.show()

	ask_for_another_walk = input("Do you want another walk? (y/n): ")
	if ask_for_another_walk == 'n':
		break

"""
Apropos Farben:
plot_color_gradients('Sequential',
                     ['Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
                      'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
                      'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn'])

https://matplotlib.org/3.5.0/tutorials/colors/colormaps.html
"""