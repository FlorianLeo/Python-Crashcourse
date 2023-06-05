class Settings:
	"""A class to store settings for Target Practise Game."""

	def __init__(self):
		"""Initialize the game's settings."""
		# Screen settings
		self.screen_x_dimension = 900
		self.screen_y_dimension = 1_400
		self.screen_bg_color = (230, 230, 230)
		# Ship settings
		self.ship_speed = 2.5
		self.ship_limit = 5
		# Bullet settings
		self.bullet_speed = 7.5
		self.bullet_widht = 15
		self.bullet_height = 3
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 10
		# Target settings
		self.target_speed = 2.0
		self.target_direction = 1