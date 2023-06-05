import pygame
# When you use sprites, you can group related elements in a game,
# and act on all the grouped elements at once
from pygame.sprite import Sprite

class Raindrop(Sprite):
	"""
	A Class to represent a Rectangle which holds
	the image of a single raindrop in a fleet of raindrops.
	"""

	def __init__(self, raindrops_game):
		"""Initialize the raindrop and set its starting position."""
		super().__init__()
		self.screen = raindrops_game.screen
		self.settings = raindrops_game.settings

		# Load the raindrop image and set its rectangle attribute.
		self.image = pygame.image.load('Images/raindrop.png')
		self.rect = self.image.get_rect()

		# Start each new raindrop near the top left of the screen.
		self.rect.x, self.rect.y = self.rect.size

		# Store the Rectangle's exact horizontal position
		# BTW - this Rectangle holds the image of the raindrop
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

	def update(self):
		"""Move the raindrop to the bottom until it disapears."""
		self.y += self.settings.raindrop_falling_speed
		self.rect.y = self.y