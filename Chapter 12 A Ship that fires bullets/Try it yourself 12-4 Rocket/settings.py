class Settings:
	"""A class to store all the settings for Alien Invasion."""

	def __init__(self):
		"""Initialize the game's settings."""
		# Screen settings
		self.screen_width = 1_200
		self.screen_height = 800
		self.bg_color = (50, 50, 50)
		# Ship settings
		self.rocket_speed = 2.5