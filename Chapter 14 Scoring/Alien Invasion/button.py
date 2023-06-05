import pygame.font

class Button:
	def __init__(self, ai_game, msg):
		"""Initialize button attributes."""
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()

		# Set the dimension and properties of the button.
		self.button_width, self.button_height = 200, 50
		self.button_color = (0, 255, 0)
		self.button_text_color = (255, 255, 255)
		self.button_font = pygame.font.SysFont(None, 48)

		# Build the button's Rectangle object and center it
		self.rect = pygame.Rect(0, 0, self.button_width, self.button_height)
		self.rect.center = self.screen_rect.center

		# The button message needs to be prepped only once.
		self._prep_msg(msg)

	def _prep_msg(self, msg):
		"""Turn msg into a rendered image and center text on the button."""
		# The call to render the font. Pass the Text (msg), turn antialiasing on, pass the font-color, pass the background-color
		self.msg_image = self.button_font.render(msg, True, self.button_text_color, self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

	def draw_button(self):
		# Draw blank button and then draw message.
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)