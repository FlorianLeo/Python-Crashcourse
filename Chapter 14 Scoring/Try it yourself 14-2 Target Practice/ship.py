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
		self.rect.midleft = self.screen_rect.midleft
		# Store a decimal value for the ship's horizontal position.
		self.y = float(self.rect.y)

		# Movement flag
		self.moving_up = False
		self.moving_down = False

	def update(self):
		"""Update the ship's position based on the movement flags."""
		# Update the ship's Rectrangle's x value.
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.y += self.settings.ship_speed
		if self.moving_up and self.rect.top > 0:
			self.y -= self.settings.ship_speed

		# Update rect object from self.x.
		self.rect.y = self.y

	def blitme(self):
		"""Draw the ship at its current location by using the blit-function"""
		self.screen.blit(self.ships_image, self.rect)