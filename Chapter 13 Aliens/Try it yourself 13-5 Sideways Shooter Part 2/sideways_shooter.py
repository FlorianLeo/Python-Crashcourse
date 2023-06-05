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
# Import the Alien
from alien import Alien

# The whole game starts out as a class by itself
class SidewaysShooter:
	"""overall class to manage game assets and behavior"""

	def __init__(self):
		"""Initialize the game, and create game resoursces."""
		pygame.init()
		# Make various settings available from the file settings.py and the class Settings
		self.settings = Settings()
		self.screen = pygame.display.set_mode((self.settings.screen_x_dimension, self.settings.screen_y_dimension))
		pygame.display.set_caption("Sideways Shooter")
		# Make the spaceship available from the file ship.py and the class Ship. The self argument here
		# refers to the current instance of Class AlienInvasion
		self.ship = Ship(self)
		# Make a group to store live bullets that have been fired
		self.bullets = pygame.sprite.Group()
		# Make a group to store aliens
		self.aliens = pygame.sprite.Group()
		# Create the aliens
		self._create_fleet_of_aliens()

	def run_game(self):
		"""Start the main loop for the game."""
		while True:
			# Watch for keyboard and mouse events.
			self._check_events()
			# Watch for ship's movements.
			self.ship.update()
			# Watch for bullets.
			self._update_bullets()
			# Watch for aliens.
			self._update_aliens()
			# Redraw the screen according to latest position of objects
			self._update_screen()

#############################
# Variety of helper-classes #
#############################
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
		if event.key == pygame.K_UP:
			self.ship.moving_up = True
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = True
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()
		elif event.key == pygame.K_q:
			sys.exit()

	def _check_keyup_events(self, event):
		"""Respond to key releases."""
		if event.key == pygame.K_UP:
			self.ship.moving_up = False
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = False

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
			if bullet.rect.right >= self.settings.screen_x_dimension:
				self.bullets.remove(bullet)
		#print(len(self.bullets))
		self._check_bullet_alien_collision()

	def _check_bullet_alien_collision(self):
		"""Respond to bullet-alien collisions."""
		# Check for any bullets that have hit aliens
		# and if so, get rid of the bullet and the alien.
		collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

		if not self.aliens:
			self.bullets.empty()
			self._create_fleet_of_aliens()

	def _update_aliens(self):
		"""
		Check if the fleet is at an edge,
			then update the positions of all aliens in the fleet.
		"""
		self._check_fleet_edges()
		self.aliens.update()

	def _create_fleet_of_aliens(self):
		"""Create a fleet of aliens."""
		# Create an alien and find the number of aliens in a colum.
		# spacing between each alien is equal to one alien height.
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		available_space_y = self.settings.screen_y_dimension - (2 * alien_height)
		number_aliens_y = available_space_y // (2 * alien_height)

		# Determine the number of colums of aliens that fit on the screen.
		ship_width = self.ship.rect.width
		available_space_x = (self.settings.screen_x_dimension - (3 * alien_width) - ship_width)
		number_colums = available_space_x // (2 * alien_width)

		# Create full fleet of aliens
		for colum_number in range(number_colums):
			for alien_number in range(number_aliens_y):
				# Create the alien and place it in the row.
				self._create_alien(alien_number, colum_number)

	def _create_alien(self, alien_number, colum_number):
		"""Create an alien and palce it in the row."""
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		alien.y = alien_height + 2 * alien_height * alien_number
		alien.rect.y = alien.y
		alien.rect.x = (self.settings.screen_x_dimension // 2) + 2 * alien.rect.width * colum_number
		self.aliens.add(alien)

	def _check_fleet_edges(self):
		"""Respond appropriately if any aliens have reached an edge."""
		for alien in self.aliens.sprites():
			if alien.check_edges():
				self._change_fleet_direction()
				break

	def _change_fleet_direction(self):
		"""Drop the entire fleet and change the fleet's direction."""
		for alien in self.aliens.sprites():
			alien.rect.x -= self.settings.fleet_drop_speed
		self.settings.fleet_direction *= -1

	def _update_screen(self):
		"""Update the images on the screen, and flip to the new screen."""
		# Redraw the screen during each pass through the loop, and fill it with the color
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()
		# Redraw the bullets that have been fired
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		# Redraw the aliens
		self.aliens.draw(self.screen)
		# Make the most recently drawn screen visible.
		pygame.display.flip()

if __name__ == '__main__':
	# Make a game instance, and run the game.
	sws = SidewaysShooter()
	sws.run_game()