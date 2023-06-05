import pygame
# When you use sprites, you can group related elements in a game,
# and act on all the grouped elements at once
from pygame.sprite import Sprite

# Since Alien is supposed to be a child, the parent (Sprite) must be named in parentheses
class Alien(Sprite):
	"""A class to represent a single alien in the fleet."""
	def __init__(self, sws_game):
		"""Initialize the alien and set its starting position."""
		# We use super to inherit properly from Class Sprite which is imported from pygame.sprite
		super().__init__()
		self.screen = sws_game.screen
		self.settings = sws_game.settings
		# Get the size of the whole game's screen
		self.screen_rect = self.screen.get_rect()

		# Load the alien bitmagp to the image-attribute
		self.image = pygame.image.load('Images/alien.bmp')
		# Create a Rectangle with the exact dimensions taken from the image-attribute (58 by 60)
		self.rect = self.image.get_rect()

		# Start each new Rectangle with it's right top corner margins
		# right from screenboarder: 60 pixels
		# top from screenboarder: 58 pixels
		self.rect.x = (self.settings.screen_x_dimension - self.rect.width)
		self.rect.y = self.rect.height

		# Store the alien's exact horizontal position.
		self.y = float(self.rect.y)

	def check_edges(self):
		"""Return True if an alien is on the top or bottom border of the screen."""
		# Check if the Rectangle for an alien touches top or bottom side of the whole game's screen
		if self.rect.top <= 0 or self.rect.bottom >= self.screen_rect.bottom:
			return True

	def update(self):
		"""Move the alien up or down."""
		# Change the movement by incrementing either with
		# the alien_speed with positive fleet_direction = 1
		# the alien_speed with negative fleet-direction = -1
		self.y += (self.settings.alien_speed * self.settings.fleet_direction)
		self.rect.y = self.y