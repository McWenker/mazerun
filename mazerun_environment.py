import pygame
import graphics
import guiBase

class SceneBase():
	
	def __init__(self):
		self.next = self
		
	def process_input(self):
		pass
		
	def update(self):
		pass
		
	def render(self):
		pass
		
	def button_logic(self):
		pass
		
	def terminate(self):
		pygame.quit()
		
class GUI(SceneBase):
	
	def __init__(self):
		SceneBase.__init__(self)
		self.surface = graphics.SCREEN
		self.surface.fill((30,30,30))
		self.gui_BackG = pygame.sprite.Group()
		self.gui_Action_list = pygame.sprite.Group()
		self.gui_Hero_list = pygame.sprite.Group()
		self.misc_list = pygame.sprite.Group()
		
		self.bottom_bar = guiBase.VisualElement(0,graphics.HEIGHT-80,graphics.WIDTH,80,(200,200,200))
		self.left_bar = guiBase.VisualElement(0,0,5,graphics.HEIGHT,(200,200,200))
		self.right_bar = guiBase.VisualElement(graphics.WIDTH-5,0,5,graphics.HEIGHT,(200,200,200))
		self.top_bar = guiBase.VisualElement(0,0,graphics.WIDTH,5,(200,200,200))
		self.action_square1 = guiBase.ClickableElement(5,graphics.HEIGHT-75,70,70,(220,48,48))
		self.action_square2 = guiBase.ClickableElement(80,graphics.HEIGHT-75,70,70,(220,48,48))
		self.action_square3 = guiBase.ClickableElement(155,graphics.HEIGHT-75,70,70,(220,48,48))
		self.action_square4 = guiBase.ClickableElement(230,graphics.HEIGHT-75,70,70,(220,48,48))
		self.action_square5 = guiBase.ClickableElement(305,graphics.HEIGHT-75,70,70,(220,48,48))
		self.hero_class1 = guiBase.ClickableElement(380,graphics.HEIGHT-75,25,25,(255,236,139))
		self.hero_class2 = guiBase.ClickableElement(410,graphics.HEIGHT-75,25,25,(255,236,139))
		self.hero_class3 = guiBase.ClickableElement(440,graphics.HEIGHT-75,25,25,(255,236,139))
		self.menu_button = guiBase.ClickableElement(380,graphics.HEIGHT-45,85,40,(45,153,70))
		
		self.gui_BackG.add(self.bottom_bar,self.top_bar,self.left_bar,self.right_bar)
		self.gui_Action_list.add(self.action_square1,self.action_square2,self.action_square3,
			self.action_square4,self.action_square5)
		self.gui_Hero_list.add(self.hero_class1,self.hero_class2,self.hero_class3)
		self.misc_list.add(self.menu_button)
		
	def process_input(self):
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				self.button_logic()
			if event.type == pygame.QUIT:
				self.terminate()
				
	def button_logic(self):
		for s in self.gui_Action_list and self.gui_Hero_list and self.misc_list:
			if s.rect.collidepoint(pygame.mouse.get_pos()):
				pass
	
	def update(self):
		pass
		
	def render(self):
		self.gui_Action_list.draw(self.surface)
		self.gui_Hero_list.draw(self.surface)
		self.misc_list.draw(self.surface)
		for s in self.gui_Action_list:
			s.on_hover(s.highlight)
		for s in self.gui_Hero_list:
			s.on_hover(s.lowlight)
		for s in self.misc_list:
			s.on_hover(s.highlight)