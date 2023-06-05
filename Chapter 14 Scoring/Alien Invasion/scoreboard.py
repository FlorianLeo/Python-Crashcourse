import pygame.font

class Scoreboard:
	"""A class to report scoring information."""

	def __init__(self, ai_game):
		"""Initialize scorekeeping attributes."""
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = ai_game.settings
		self.stats = ai_game.stats
		# Font settings for scoring information.
		# Text Color
		self.text_color = (30, 30, 30)
		# Instantiate a font object
		self.font = pygame.font.SysFont(None, 48)
		# Prepare the initial score image. Remember: python must create an image from the text
		# since it can't display the text, but rather an image. Do this job with a helper-method
		# prep the initial score images
		self._scores_image_and_rectangle()
		self.prep_high_score()

	def _scores_image_and_rectangle(self):
		"""Turn the score into a rendered image."""
		# Remember: python must create an image from the text
		# Get the numerical value from line 14 from the game_stats.py-file and turn it into a string
		rounded_score = round(self.stats.score, -1)
		score_str = "{:,}".format(rounded_score)
		# Create the image from the String
		# The call to render the font. Pass the Text (msg), turn antialiasing on, pass the font-color, pass the background-color
		self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
		# Get the dimensions of the scores image and make a rectangle-object from it
		self.score_rect = self.score_image.get_rect()
		# Position the Rectangle's right side minus 20 pixels from the screen's right edge
		self.score_rect.right = self.screen_rect.right - 20
		# Position the Rectangle's top side plus 20 pixels form the screen's top edge
		self.score_rect.top = 20

	def show_score(self):
		"""Method to make the score appear to the screen"""
		self.screen.blit(self.score_image, self.score_rect)