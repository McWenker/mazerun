import pygame

class VisualElement(pygame.sprite.Sprite):

	def __init__(self, x, y, width, height, color):
		pygame.sprite.Sprite.__init__(self)
		self.width = width
		self.height = height
		self.color = color
		
		self.image = pygame.Surface([self.width, self.height])
		self.image.fill(self.color)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		
	def highlight(self):
		highlighted = [x+30 for x in self.color if x < 225]
		self.image.fill(highlighted)
		
	def lowlight(self):
		lowlighted = [x-30 for x in self.color if x > 30]
		self.image.fill(lowlighted)
		
	def fade_in(self):
		pass
		
	def fade_out(self):
		pass
		
class ClickableElement(VisualElement):
	'''a GUI class for handling mouse interaction'''
	
	def __init__(self, x, y, width, height, color):
		VisualElement.__init__(self, x, y, width, height, color)
		
	def on_hover(self, function, *args):
		if self.rect.collidepoint(pygame.mouse.get_pos()):
			function(*args)
		else: self.image.fill(self.color)
		
	def on_click(self, function):
		pass