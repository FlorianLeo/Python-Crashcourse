class Settings:
	"""A class to store all the settings for Alien Invasion."""

	def __init__(self):
		"""Initialize the game's settings."""
		# Screen settings
		self.screen_width = 1_200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)
		# Ship settings
		self.ship_speed = 2.5
		self.ship_limit = 5
		# Bullet settings
		self.bullet_speed = 7.5
		self.bullet_widht = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 10
		# Alien Settings
		# the direction of 1 represents moving to the right; -1 left
		self.fleet_direction = 1
		self.alien_speed = 1.0
		self.fleet_drop_speed = 10
