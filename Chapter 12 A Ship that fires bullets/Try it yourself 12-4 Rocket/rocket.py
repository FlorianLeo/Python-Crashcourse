import pygame

class Rocket:
	"""A Class to model/manage the Spaceship"""

	def __init__(self, rocket_game):
		"""Initialize the Rocket and set its starting position."""
		self.screen = rocket_game.screen
		self.settings = rocket_game.settings
		self.screen_rect = rocket_game.screen.get_rect()
		# Load the Rocket image and get its rect.
		self.image = pygame.image.load('Images/rocket.png')
		self.rect = self.image.get_rect()
		# Start each new Rocket at the center of the screen.
		self.rect.center = self.screen_rect.center
		# Store a decimal value for the rocket's horizontal and vertical position.
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)
		# Movement flag
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

	def update(self):
		"""Update the rocket's position based on the movement flags."""
		# Update the rocket's x and y values, not the rect.
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.rocket_speed
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.y += self.settings.rocket_speed
		if self.moving_left and self.rect.left > 0:
			self.x -= self.settings.rocket_speed
		if self.moving_up and self.rect.top > 0:
			self.y -= self.settings.rocket_speed

		# Update rect object from self.x.
		self.rect.x = self.x
		# Update rect object from self.y.
		self.rect.y = self.y

	def blitme(self):
		"""Draw the rocket at its current location by using the blit-function"""
		self.screen.blit(self.image, self.rect)