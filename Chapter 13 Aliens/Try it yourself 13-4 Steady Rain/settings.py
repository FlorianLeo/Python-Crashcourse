class Settings:
	"""A class to store all the settings for Stars."""

	def __init__(self):
		"""Initialize the game's settings."""
		# Screen settings
		self.screen_x_dimension = 1_200
		self.screen_y_dimension = 800
		self.bg_color = (30, 30, 30)
		# Raindrop Settings
		self.raindrop_falling_speed = 5.0