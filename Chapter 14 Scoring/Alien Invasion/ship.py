import pygame

class Ship:
	"""A Class to model/manage the Spaceship"""

	def __init__(self, ai_game):
		"""Initialize the ship and set its starting position."""
		# The Window/Screen from Class AlienInvasion is assigned to an attribute of Class Ship (Ship.screen)
		# since we need to access some values later from within this class.
		self.screen = ai_game.screen
		# The settings from Class AlienInvasion is assigned to an attribute of Class Ship (Ship.settings)
		self.settings = ai_game.settings
		# The Dimensions from the Window/Screen from Class AlienInvation become an attribute of Class Ship (Ship.screen_rect)
		self.screen_rect = ai_game.screen.get_rect()

		# Load the ship bitmagp to the image-attribute (Ship.ships_image)
		self.ships_image = pygame.image.load('Images/ship.bmp')
		# Store exact dimensions from the image-attribute (Ship.rect)
		self.rect = self.ships_image.get_rect()

		# Find the value from the Windows/Screen Middle and Bottom and make it an attriubte of Class Ship (Ship.rect.midbottom)
		self.rect.midbottom = self.screen_rect.midbottom
		# Store a decimal value for the ship's horizontal position.
		self.x = float(self.rect.x)

		# Movement flag
		self.moving_right = False
		self.moving_left = False

	def update(self):
		"""Update the ship's position based on the movement flags."""
		# Update the ship's Rectrangle's x value.
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
		if self.moving_left and self.rect.left > 0:
			self.x -= self.settings.ship_speed

		# Update rect object from self.x.
		self.rect.x = self.x

	def blitme(self):
		"""Draw the ship at its current location by using the blit-function"""
		self.screen.blit(self.ships_image, self.rect)

	def center_ship(self):
		"""Center the ship on the screen."""
		self.rect.midbottom = self.screen_rect.midbottom
		self.x = float(self.rect.x)