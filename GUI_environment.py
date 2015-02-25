import pygame
import visual_ele as GUI_env
from constants import *

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
	
	def __init__(self, surface):
		SceneBase.__init__(self)
		self.surface = surface
		self.gui_BackG = pygame.sprite.Group()
		self.gui_Action_list = pygame.sprite.Group()
		self.gui_Hero_list = pygame.sprite.Group()
		self.misc_list = pygame.sprite.Group()
		
		self.bottom_bar = GUI_env.VisualElement(0,SCREEN_HEIGHT-80,SCREEN_WIDTH,80,(GUI_WHT))
		self.left_bar = GUI_env.VisualElement(0,0,5,SCREEN_HEIGHT,(GUI_WHT))
		self.right_bar = GUI_env.VisualElement(SCREEN_WIDTH-5,0,5,SCREEN_HEIGHT,(GUI_WHT))
		self.top_bar = GUI_env.VisualElement(0,0,SCREEN_WIDTH,5,(GUI_WHT))
		self.action_square1 = GUI_env.ClickableElement(5,SCREEN_HEIGHT-75,70,70,(GUI_RED))
		self.action_square2 = GUI_env.ClickableElement(80,SCREEN_HEIGHT-75,70,70,(GUI_RED))
		self.action_square3 = GUI_env.ClickableElement(155,SCREEN_HEIGHT-75,70,70,(GUI_RED))
		self.action_square4 = GUI_env.ClickableElement(230,SCREEN_HEIGHT-75,70,70,(GUI_RED))
		self.action_square5 = GUI_env.ClickableElement(305,SCREEN_HEIGHT-75,70,70,(GUI_RED))
		self.hero_class1 = GUI_env.ClickableElement(380,SCREEN_HEIGHT-75,25,25,(GUI_YEL))
		self.hero_class2 = GUI_env.ClickableElement(410,SCREEN_HEIGHT-75,25,25,(GUI_YEL))
		self.hero_class3 = GUI_env.ClickableElement(440,SCREEN_HEIGHT-75,25,25,(GUI_YEL))
		self.menu_button = GUI_env.ClickableElement(380,SCREEN_HEIGHT-45,85,40,(GUI_GRN))
		self.hero_button = GUI_env.ClickableElement(470,SCREEN_HEIGHT-75,70,70,(GUI_BLK))
		
		self.gui_BackG.add(self.bottom_bar,self.top_bar,self.left_bar,self.right_bar)
		self.gui_Action_list.add(self.action_square1,self.action_square2,self.action_square3,
			self.action_square4,self.action_square5)
		self.gui_Hero_list.add(self.hero_class1,self.hero_class2,self.hero_class3)
		self.misc_list.add(self.menu_button,self.hero_button)
		
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
		self.gui_BackG.draw(self.surface)
		self.gui_Action_list.draw(self.surface)
		self.gui_Hero_list.draw(self.surface)
		self.misc_list.draw(self.surface)
		for s in self.gui_Action_list:
			s.on_hover(s.highlight)
		for s in self.gui_Hero_list:
			s.on_hover(s.lowlight)
		for s in self.misc_list:
			s.on_hover(s.highlight)