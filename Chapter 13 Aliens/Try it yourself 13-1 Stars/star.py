import pygame
# When you use sprites, you can group related elements in a game,
# and act on all the grouped elements at once
from pygame.sprite import Sprite

class Star(Sprite):
	"""A Class to represent a single star in a fleet of stars."""

	def __init__(self, stars_game):
		"""Initialize the star and set its starting position."""
		super().__init__()
		self.screen = stars_game.screen
		self.settings = stars_game.settings

		# Load the star image and set its rectangle attribute.
		self.image = pygame.image.load('Images/star.png')
		self.rect = self.image.get_rect()

		# Start each new star near the top left of the screen.
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		# Store the stars exact horizontal position.
		self.x = float(self.rect.x)