# We use tools from the sys to exit the game wen the player quits
import sys
# pygame contains the functinality we need to mak a game
import pygame
# Import settings for the game
from settings import Settings
# Import the space-ship
from ship import Ship
# Import the Bullet
from bullet import Bullet

# The whole game starts out as a class by itself
class AlienInvasion:
	"""overall class to manage game assets and behavior"""

	def __init__(self):
		"""Initialize the game, and create game resoursces."""
		pygame.init()
		# Make various settings available from the file settings.py and the class Settings
		self.settings = Settings()
		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("Alien Invasion")
		# Make the spaceship available from the file ship.py and the class Ship
		self.ship = Ship(self)
		# Make a group to store live bullets that have been fired
		self.bullets = pygame.sprite.Group()

	def run_game(self):
		"""Start the main loop for the game."""
		while True:
			# Watch for keyboard and mouse events.
			self._check_events()
			# Watch for ship's movements.
			self.ship.update()
			# Watch for bullets.
			self._update_bullets()
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
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)

	def _check_keydown_events(self, event):
		"""Respond to keypresses."""
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = True
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()
		elif event.key == pygame.K_q:
			sys.exit()

	def _check_keyup_events(self, event):
		"""Respond to key releases."""
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False

	def _fire_bullet(self):
		"""Create a new bullet and add it to the bullets group."""
		# Create a new bullet only if no more than the allowed bullets
		# are currently in the game
		if len(self.bullets) < self.settings.bullets_allowed:
			# Instantiate a new bullet from the class Bullet
			new_bullet = Bullet(self)
			# Add the new object to the group of bullets
			self.bullets.add(new_bullet)

	def _update_bullets(self):
		"""Update the position of bullets and get rid of old bullets."""
		# Update the bullet positions
		self.bullets.update()
		# Get rid of bullets in that have disappeared at the top
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)
		#print(len(self.bullets))


	def _update_screen(self):
		"""Update the images on the screen, and flip to the new screen."""
		# Redraw the screen during each pass through the loop, and fill it with the color
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()
		# Redraw the bullets that have been fired
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		# Make the most recently drawn screen visible.
		pygame.display.flip()

if __name__ == '__main__':
	# Make a game instance, and run the game.
	ai = AlienInvasion()
	ai.run_game()