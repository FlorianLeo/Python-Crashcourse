# We use tools from the sys to exit the game wen the player quits
import sys
# pygame contains the functinality we need to mak a game
import pygame
# Import settings for the game
from settings import Settings
# Import the star
from raindrop import Raindrop

# The whole game starts out as a class by itself
class SteadyRainGame:
	"""overall class to manage game assets and behavior"""

	def __init__(self):
		"""Initialize the game, and create game resoursces."""
		pygame.init()
		# Make various settings available from the file settings.py and the class Settings
		self.settings = Settings()
		self.screen = pygame.display.set_mode((self.settings.screen_x_dimension, self.settings.screen_y_dimension))
		pygame.display.set_caption('Steady Rain game')
		# Make a group to store raindrops
		self.raindrops = pygame.sprite.Group()

		self._create_fleet_of_raindrops()

	def _create_fleet_of_raindrops(self):
		"""Create a fleet of raindrop."""
		# Create a raindrop and find the maximum number of raindrops possible in a row
		# according to the size of the image and the available screen-size.
		# spacing between each raindrop is equal to one raindrop's width.
		raindrop = Raindrop(self)
		raindrop_width = raindrop.rect.width
		# The margin shall be the width of 1 raindrop, and since there is left and right margin
		# the available space equals screen-width minus twice the width of a raindrop
		available_space_x = self.settings.screen_x_dimension - (2 * raindrop_width)
		# The spacing between raindrop shall be 1 width of 1 raindrop = the space for 1 raindrop is twice it's width
		# Divide the available space by twice the width of 1 raindrop.
		# Use the 'floor-division' (//) which returns an integer and drops any remainder
		total_of_raindrops_possible_in_x = available_space_x // (2 * raindrop_width)
		# Create full fleet of stars
		# the range-function will return values beginning with 1 up to the maximum number
		# of stars possible which was calculated a few lines above
		for id_of_current_raindrop in range(total_of_raindrops_possible_in_x):
			# Create the raindrop by calling the helper-method to create a raindrop and place it in the row after creation
			self._create_raindrop(id_of_current_raindrop)

	def _create_raindrop(self, id_of_current_raindrop):
		"""Create a single raindrop and place it in the row."""
		raindrop = Raindrop(self)
		raindrop_width = raindrop.rect.width
		raindrop.x = raindrop_width + 2 * raindrop_width * id_of_current_raindrop
		raindrop.rect.x = raindrop.x
		self.raindrops.add(raindrop)

	def run_game(self):
		"""Start the main loop for the game."""
		while True:
			# Watch for keyboard and mouse events.
			self._check_events()
			# Update the positions of the raindrops.
			self._update_raindrop()
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

	def _update_raindrop(self):
		"""Make the raindrop fall"""
		self.raindrops.update()
		# Get rid of raindrops that have disapeared
		for raindrop in self.raindrops.copy():
			if raindrop.rect.top > self.settings.screen_y_dimension:
				self.raindrops.remove(raindrop)
		# Once the row of raindrops has disappeared let new one fall
		if len(self.raindrops) == 0:
			self._create_fleet_of_raindrops()

	def _update_screen(self):
		"""Update the images on the screen, and flip to the new screen."""
		# Redraw the screen during each pass through the loop, and fill it with the color
		self.screen.fill(self.settings.bg_color)
		# Redraw the raindrop
		self.raindrops.draw(self.screen)
		# Make the most recently drawn screen visible.
		pygame.display.flip()

if __name__ == '__main__':
	# Make a game instance, and run the game.
	srg = SteadyRainGame()
	srg.run_game()