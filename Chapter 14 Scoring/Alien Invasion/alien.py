import pygame
# When you use sprites, you can group related elements in a game,
# and act on all the grouped elements at once
from pygame.sprite import Sprite

# Since Alien is supposed to be a child, the parent (Sprite) must be named in parentheses
class Alien(Sprite):
	"""A class to represent a single alien in the fleet."""
	def __init__(self, ai_game):
		"""Initialize the alien and set its starting position."""
		# We use super to inherit properly from Class Sprite which is imported from pygame.sprite
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings

		# Load the alien bitmagp to the image-attribute
		# Create a Rectangle with the exact dimensions taken from the image-attribute (60 by 58)
		# and place the image in this Rectangle
		self.image = pygame.image.load('Images/alien.bmp')
		self.rect = self.image.get_rect()

		# Start each new Rectangle with it's left top corner margins
		# left from screenboarder: 60 pixels
		# top from screenboarder: 58 pixels
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# Store the alien's exact horizontal position.
		self.x = float(self.rect.x)

	def check_edges(self):
		"""Return True if an alien is on the left or right border of the screen."""
		# Get the size of the whole game's screen
		screen_rect = self.screen.get_rect()
		# Check if the Rectangel for an alien touches left or right side of the whole game's screen
		if self.rect.left <= 0 or self.rect.right >= screen_rect.right:
			return True

	def update(self):
		"""Move the alien to the right or to the left."""
		# Change the movement by incrementing either with
		# the alien_speed with positive fleet_direction = 1
		# the alien_speed with negative fleet-direction = -1
		self.x += (self.settings.alien_speed * self.settings.fleet_direction)
		self.rect.x = self.x