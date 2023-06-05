# We use tools from the sys to exit the game wen the player quits
import sys
# pygame contains the functinality we need to mak a game
import pygame
# Import settings Class for the game
from settings import Settings
# Import the Ship Class
from ship import Ship
# Import the Bullet Class
from bullet import Bullet
# Import the Target
from rectangle import Rectangle

# The whole game starts out as a class by itself
class TargetPractise:
	"""overall class to manage game assets and behavior"""

	def __init__(self):
		"""Initialize the game, and create game resoursces."""
		pygame.init()
		# Make various settings available from the file settings.py and the class Settings
		self.settings = Settings()
		# Create the window/screen for the game
		self.screen = pygame.display.set_mode((self.settings.screen_x_dimension, self.settings.screen_y_dimension))
		pygame.display.set_caption("Target Practise")
		# Make the spaceship available from the file ship.py and the class Ship. The self argument here
		# refers to the current instance of Class TargetPractise
		self.ship = Ship(self)
		# Create the target
		self.target = Rectangle(self)

	def run_game(self):
		"""Start the main loop for the game."""
		while True:
			# Watch for keyboard and mouse events.
			self._check_events()
			# Watch for ship's movements.
			self.ship.update()
			# check the target moving.
			self._update_target()
			# Redraw the screen according to latest position of objects
			self._update_screen()

	# a helper method does work inside a class BUT IS NOT meant to be called through instanciation!
	def _check_events(self):
		"""Respond the keyboard or mouse input events."""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			# React to keystrokes which are taken from the helper-classes
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)

	# a helper method does work inside a class BUT IS NOT meant to be called through instanciation!
	def _check_keydown_events(self, event):
		"""Respond to keypresses."""
		if event.key == pygame.K_UP:
			self.ship.moving_up = True
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = True
		#elif event.key == pygame.K_SPACE:
		#	self._fire_bullet()
		elif event.key == pygame.K_q:
			sys.exit()

	# a helper method does work inside a class BUT IS NOT meant to be called through instanciation!
	def _check_keyup_events(self, event):
		"""Respond to key releases."""
		if event.key == pygame.K_UP:
			self.ship.moving_up = False
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = False

	# a helper method does work inside a class BUT IS NOT meant to be called through instanciation!
	def _update_target(self):
		"""
		Check if the target is at an edge,
			then update the position of the target.
		"""
		self._check_target_edges()
		self.target.update()

	# a helper method does work inside a class BUT IS NOT meant to be called through instanciation!
	def _check_target_edges(self):
		"""Respond appropriately if target has reached an edge."""
		if self.target.check_edges():
			self._change_target_direction()

	# a helper method does work inside a class BUT IS NOT meant to be called through instanciation!
	def _change_target_direction(self):
		"""change the targets's direction."""
		self.settings.target_direction *= -1

	# a helper method does work inside a class BUT IS NOT meant to be called through instanciation!
	def _update_screen(self):
		"""Update the images on the screen, and flip to the new screen."""
		# Redraw the screen during each pass through the loop, and fill it with the color
		self.screen.fill(self.settings.screen_bg_color)
		self.ship.blitme()
		# Redraw the target
		self.target.draw_rectangle()
		# Make the most recently drawn screen visible.
		pygame.display.flip()

if __name__ == '__main__':
	# Make a game instance, and run the game.
	tp = TargetPractise()
	tp.run_game()