import pygame
# When you use sprites, you can group related elements in a game,
# and act on all the grouped elements at once
from pygame.sprite import Sprite

# Since Bullet is supposed to be a child, the parent (Sprite) must be named in parentheses
class Bullet(Sprite):
	"""A class to manage bullets fired from the ship"""
	def __init__(self, ai_game):
		"""create a bullet object at the ship's current position."""
		# We use super to inherit properly from Class Sprite which is imported from pygame.sprite
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.color = self.settings.bullet_color

		# Create a bullet Rectangle at (0, 0) and then set the correct position.
		# The bullet isn't based on an image, so we have to build a Rectangle
		# from scrath using the pygame.Rect() class.
		self.rect = pygame.Rect(0, 0, self.settings.bullet_widht, self.settings.bullet_height)

		# We initialized the Rectangle at x=0 and y=0, and other properties - BUT
		# We need to move it to the correct location = to the ship's position
		# We set the midtop attribute to match the ship's midtop attribute
		self.rect.midtop = ai_game.ship.rect.midtop

		# Store the bullet's y position as a decimal value.
		self.y = float(self.rect.y)

	def update(self):
		"""Move the bullet up the screen."""
		# Update the decimal position ot the Rectangle/Bullet.
		self.y -= self.settings.bullet_speed
		# Update the position of the Rectangle/Bullet.
		self.rect.y = self.y

	def draw_bullet(self):
		"""Draw the Rectrangle/Bullet to the screen."""
		pygame.draw.rect(self.screen, self.color, self.rect)