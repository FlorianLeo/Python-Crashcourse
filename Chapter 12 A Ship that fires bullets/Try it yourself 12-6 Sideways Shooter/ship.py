import pygame

class Ship:
	"""A Class to model/manage the Spaceship"""

	def __init__(self, sws_game):
		"""Initialize the ship and set its starting position."""
		self.screen = sws_game.screen
		self.settings = sws_game.settings
		self.screen_rect = sws_game.screen.get_rect()
		# Load the ship image and get its rect.
		self.image = pygame.image.load('Images/ship.bmp')
		self.rect = self.image.get_rect()
		# Start each new ship at the left center of the screen.
		self.rect.midleft = self.screen_rect.midleft
		# Store a decimal value for the ship's vertical position.
		self.y = float(self.rect.y)
		# Movement flag
		self.moving_down = False
		self.moving_up = False

	def update(self):
		"""Update the ship's position based on the movement flags."""
		# Update the ship's y value, not the rect.
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.y += self.settings.ship_speed
		if self.moving_up and self.rect.top > 0:
			self.y -= self.settings.ship_speed

		# Update rect object from self.x.
		self.rect.y = self.y

	def blitme(self):
		"""Draw the ship at its current location by using the blit-function"""
		self.screen.blit(self.image, self.rect)