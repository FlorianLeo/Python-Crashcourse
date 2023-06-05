# We use tools from the sys to exit the game wen the player quits
import sys
# pygame contains the functinality we need to mak a game
import pygame
# Import settings for the game
from settings import Settings
# Import the star
from star import Star
# Radomize whatever
from random import randint

# The whole game starts out as a class by itself
class StarsgameV2:
	"""overall class to manage game assets and behavior"""

	def __init__(self):
		"""Initialize the game, and create game resoursces."""
		pygame.init()
		# Make various settings available from the file settings.py and the class Settings
		self.settings = Settings()
		self.screen = pygame.display.set_mode((self.settings.screen_x_dimension, self.settings.screen_y_dimension))
		pygame.display.set_caption('Better Stars game')
		# Make a group to store stars
		self.stars = pygame.sprite.Group()

		self._create_fleet_of_stars()

	def run_game(self):
		"""Start the main loop for the game."""
		while True:
			# Watch for keyboard and mouse events.
			self._check_events()
			# Redraw the screen according to latest position of objects
			self._update_screen()

	def _check_events(self):
		"""Respond the keyboard or mouse input events."""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			# React to keystrokes which are taken from the helper-classes
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)

	def _check_keydown_events(self, event):
		"""Respond to keypresses."""
		if event.key == pygame.K_q:
			sys.exit()

	def _create_fleet_of_stars(self):
		"""Create a fleet of stars."""
		# Create a star and find the number of stars in a row according
		# to the size of the image and the available screen-size.
		# spacing between each star is equal to one star width.
		star = Star(self)
		star_width = star.rect.width
		# The margin shall be the width of 1 star, and since there is left and right margin
		# the available space equals screen-width minus 2 times the width of a star
		available_space_x = self.settings.screen_x_dimension - (2 * star_width)
		# The spacing between stars shall be 1 width of 1 star = the space for 1 star is twice it's width
		# Divide the available space by twice the width of 1 star.
		# Use the 'floor-division' (//) which returns an integer and drops any remainder
		total_of_stars_possible_in_x = available_space_x // (2 * star_width)
		# Create full fleet of stars
		# the range-function will return values beginning with 1 up to the maximum number of stars possible
		# which was calculated in line 63
		for single_star in range(total_of_stars_possible_in_x):
			# Create the star by calling the helper-method to create a star and place it in the row after creation
			self._create_star(single_star)

	def _create_star(self, total_number_of_stars):
		"""Create a single star and place it in the row."""
		# Create the star
		star = Star(self)
		star_width = star.rect.width
		star.x = star_width + 2 * star_width * total_number_of_stars
		# Generate a random number for uneven spacing between stars
		random_distance_to_use = randint((star_width // -2), (star_width // 2))
		star.rect.x = (star.x + random_distance_to_use)
		self.stars.add(star)

	def _update_screen(self):
		"""Update the images on the screen, and flip to the new screen."""
		# Redraw the screen during each pass through the loop, and fill it with the color
		self.screen.fill(self.settings.bg_color)
		# Redraw the stars
		self.stars.draw(self.screen)
		# Make the most recently drawn screen visible.
		pygame.display.flip()

if __name__ == '__main__':
	# Make a game instance, and run the game.
	sg = StarsgameV2()
	sg.run_game()