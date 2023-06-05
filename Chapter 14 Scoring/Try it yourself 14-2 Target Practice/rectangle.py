import pygame

# Since Bullet is supposed to be a child, the parent (Sprite) must be named in parentheses
class Rectangle:
	"""A class to create a Rectangle"""
	def __init__(self, ai_game):
		"""create a Rectangle object at the right edge"""
		self.screen = ai_game.screen
		self.settings = ai_game.settings

		# Set the dimension and properties of the Rectangle
		self.target_x_dimension = 50
		self.target_y_dimension = 50
		self.target_color = (255, 0, 0)

		# Create a target Rectangle
		self.rect = pygame.Rect((self.settings.screen_x_dimension - self.target_x_dimension), (self.settings.screen_y_dimension // 2), self.target_x_dimension, self.target_y_dimension)

		# Store the target's y position as a decimal value.
		self.y = float(self.rect.y)

	def check_edges(self):
		"""Return True if target is on the top or bottom border of the screen."""
		# Get the size of the whole game's screen
		screen_rect = self.screen.get_rect()
		# Check if the Rectangle touches top or bottom side of the whole game's screen
		if self.rect.top <= 0 or self.rect.bottom >= screen_rect.bottom:
			return True

	def update(self):
		"""Move the target up or down."""
		# Change the movement by incrementing either with
		# the target_speed with positive target_direction = 1
		# the target_speed with negative target_direction = -1
		self.y += (self.settings.target_speed * self.settings.target_direction)
		self.rect.y = self.y

	def draw_rectangle(self):
		# Draw the Rectangle
		self.screen.fill(self.target_color, self.rect)