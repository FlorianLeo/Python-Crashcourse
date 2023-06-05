import matplotlib.pyplot as plt

from tiy_15_5_random_walk import RandomWalk

# Begin a random walk.
while True:
	# rw ist die Instanz der Klasse RandomWalk
	rw = RandomWalk()
	# rw führt die Funktion fill_walk aus
	rw.fill_walk()

	# Plot the points in the walk.
	plt.style.use('classic')
	fig, ax = plt.subplots(figsize=(6, 4), dpi=254)
	steps_for_the_walk = range(rw.num_points)

	ax.scatter(rw.x_values, rw.y_values, c=steps_for_the_walk, cmap=plt.cm.OrRd, edgecolors='none', s=1)

	# Emphasize the first and the last point.
	ax.scatter(0, 0, c='yellow', edgecolors='none', s=100)
	ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

	# remove the x and y axis
	ax.get_xaxis().set_visible(False)
	ax.get_yaxis().set_visible(False)

	plt.savefig('random_walk.png', bbox_inches='tight')
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