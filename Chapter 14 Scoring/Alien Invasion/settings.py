class Settings:
	"""A class to store all the settings for Alien Invasion."""

	def __init__(self):
		"""Initialize the game's STATIC settings."""
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
		self.alien_speed = 1.0
		self.fleet_direction = 1
		self.fleet_drop_speed = 10
		# How quickly the game speeds up
		self.speedup_scale = 1.2
		# How quickly the point value increases
		self.score_scale = 1.5

		# We need to call a method to initialize the values that need to chanbe throughout the game
		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		"""Initialize the game's DYNAMIC settings = change throughout the game."""
		self.ship_speed = 2.5
		self.bullet_speed = 7.5
		self.alien_speed = 1.0
		self.fleet_direction = 1
		self.alien_points = 50

	def increase_speed(self):
		"""Increase the speed settings."""
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.alien_speed *= self.speedup_scale
		self.alien_points = int(self.alien_points * self.score_scale)
