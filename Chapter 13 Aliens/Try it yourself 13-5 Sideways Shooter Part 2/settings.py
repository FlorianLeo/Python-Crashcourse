class Settings:
	"""A class to store all the settings for Sideways Shooter."""

	def __init__(self):
		"""Initialize the game's settings."""
		# Screen settings
		self.screen_x_dimension = 800
		self.screen_y_dimension = 1_500
		self.bg_color = (230, 230, 230)
		# Ship settings
		self.ship_speed = 1.5
		# Bullet settings
		self.bullet_speed = 7.5
		self.bullet_widht = 15
		self.bullet_height = 3
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 10
		# Alien Settings
		# the direction of 1 represents moving to the right; -1 left
		self.fleet_direction = 1
		self.alien_speed = 1.0
		self.fleet_drop_speed = 10
