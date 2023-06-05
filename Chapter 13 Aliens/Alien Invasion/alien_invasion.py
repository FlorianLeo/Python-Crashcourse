# We use tools from the sys to exit the game wen the player quits
import sys
# We need to import sleep from Python standards Library
from time import sleep
# pygame contains the functinality we need to mak a game
import pygame
# Import settings Class for the game
from settings import Settings
# Import the space-ship Class
from ship import Ship
# Import the Bullet Class
from bullet import Bullet
# Import the Alien Class
from alien import Alien
# Import the statistic Class
from game_stats import GameStats

# The whole game starts out as a class by itself
class AlienInvasion:
	"""overall class to manage game assets and behavior"""

	def __init__(self):
		"""Initialize the game, and create game resoursces."""
		pygame.init()
		# Make various settings available from the file settings.py and the class Settings
		self.settings = Settings()
		# Create the window/screen for the game
		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("Alien Invasion")
		# Make the instance from Statistics to have statistic available
		self.stats = GameStats(self)
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
			# check if player still has ships left over, and if so keep the game running
			if self.stats.game_active:
				# Watch for ship's movements.
				self.ship.update()
				# Watch for bullets.
				self._update_bullets()
				# Watch for aliens.
				self._update_aliens()
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
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = True
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()
		elif event.key == pygame.K_q:
			sys.exit()

	# a helper method does work inside a class BUT IS NOT meant to be called through instanciation!
	def _check_keyup_events(self, event):
		"""Respond to key releases."""
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False

	# a helper method does work inside a class BUT IS NOT meant to be called through instanciation!
	def _fire_bullet(self):
		"""Create a new bullet and add it to the bullets group."""
		# Create a new bullet only if no more than the allowed bullets
		# are currently in the game
		if len(self.bullets) < self.settings.bullets_allowed:
			# Instantiate a new bullet from the class Bullet
			new_bullet = Bullet(self)
			# Add the new object to the group of bullets
			self.bullets.add(new_bullet)

	# a helper method does work inside a class BUT IS NOT meant to be called through instanciation!
	def _update_bullets(self):
		"""Update the position of bullets and get rid of old bullets."""
		# Update the bullet positions
		self.bullets.update()
		# Get rid of bullets in that have disappeared at the top
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)
		#print(len(self.bullets))
		self._check_bullet_alien_collision()

	# a helper method does work inside a class BUT IS NOT meant to be called through instanciation!
	def _check_bullet_alien_collision(self):
		"""Respond to bullet-alien collisions."""
		# Check for any bullets that have hit aliens
		# and if so, get rid of the bullet and the alien.
		collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

		if not self.aliens:
			self.bullets.empty()
			self._create_fleet_of_aliens()

	# a helper method does work inside a class BUT IS NOT meant to be called through instanciation!
	def _update_aliens(self):
		"""
		Check if the fleet is at an edge,
			then update the positions of all aliens in the fleet.
		"""
		self._check_fleet_edges()
		self.aliens.update()

		# Look for alien-ship collisions and if so call the helper _ship_hit()
		if pygame.sprite.spritecollideany(self.ship, self.aliens):
			self._ship_hit()

		# Lookf for aliens that may have reached the bottom of the screen
		self._check_aliens_bottom()

	# a helper method does work inside a class BUT IS NOT meant to be called through instanciation!
	def _ship_hit(self):
		"""Respondd to the ship being hit by an alien."""
		# Restart over only if enough ships are left
		if self.stats.ships_leftover > 0:
			# Decrement the ships that are left.
			self.stats.ships_leftover -= 1

			# Get rid of any remaing aliens and bullets.
			self.aliens.empty()
			self.bullets.empty()

			# Create a new fleet and center the ship.
			self._create_fleet_of_aliens()
			self.ship.center_ship()

			# Pause the game for a few seconds.
			sleep(2)
		else:
			self.stats.game_active = False

	# a helper method does work inside a class BUT IS NOT meant to be called through instanciation!
	def _check_aliens_bottom(self):
		"""Check if any aliens have reached the bottom of the screen."""
		screen_rect = self.screen.get_rect()
		for alien in self.aliens.sprites():
			if alien.rect.bottom >= screen_rect.bottom:
				# Treat this situation the same way as if a ship was hit by an alien
				self._ship_hit()
				break

	# a helper method does work inside a class BUT IS NOT meant to be called through instanciation!
	def _create_fleet_of_aliens(self):
		"""Create a fleet of aliens."""
		# Create an alien and find the number of aliens in a row.
		# spacing between each alien is equal to one alien width.
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		available_space_x = self.settings.screen_width - (2 * alien_width)
		number_aliens_x = available_space_x // (2 * alien_width)

		# Determine the number of rows of aliens that fit on the screen.
		ship_height = self.ship.rect.height
		available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
		number_rows = available_space_y // (2 * alien_height)

		# Create full fleet of aliens
		for row_number in range(number_rows):
			for alien_number in range(number_aliens_x):
				# Create the alien and place it in the row.
				self._create_alien(alien_number, row_number)

	# a helper method does work inside a class BUT IS NOT meant to be called through instanciation!
	def _create_alien(self, alien_number, row_number):
		"""Create an alien and palce it in the row."""
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		alien.x = alien_width + 2 * alien_width * alien_number
		alien.rect.x = alien.x
		alien.rect.y = alien_height + 2 * alien.rect.height * row_number
		self.aliens.add(alien)

	# a helper method does work inside a class BUT IS NOT meant to be called through instanciation!
	def _check_fleet_edges(self):
		"""Respond appropriately if any alien shave reached an edge."""
		for alien in self.aliens.sprites():
			if alien.check_edges():
				self._change_fleet_direction()
				break

	# a helper method does work inside a class BUT IS NOT meant to be called through instanciation!
	def _change_fleet_direction(self):
		"""Drop the entire fleet and change the fleet's direction."""
		for alien in self.aliens.sprites():
			alien.rect.y += self.settings.fleet_drop_speed
		self.settings.fleet_direction *= -1

	# a helper method does work inside a class BUT IS NOT meant to be called through instanciation!
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
	ai = AlienInvasion()
	ai.run_game()