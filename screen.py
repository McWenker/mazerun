import pygame, GUI_environment
import constants as const
from pygame.locals import *

class Screen(object):

	def __init__(self):
		self.screen = pygame.display.set_mode([const.SCREEN_WIDTH,const.SCREEN_HEIGHT],
			pygame.NOFRAME+pygame.DOUBLEBUF,32)
		self.mapSurf = pygame.Surface((const.SCREEN_WIDTH,const.SCREEN_HEIGHT),
			pygame.HWSURFACE + pygame.SRCALPHA)
		self.GUISurf = pygame.Surface((const.SCREEN_WIDTH,const.SCREEN_HEIGHT),
			pygame.HWSURFACE + pygame.SRCALPHA)
		self.menuSurf = pygame.Surface((const.SCREEN_WIDTH,const.SCREEN_HEIGHT),
			pygame.HWSURFACE + pygame.SRCALPHA)
		self.spriteSurf = pygame.Surface((const.SCREEN_WIDTH,const.SCREEN_HEIGHT),
			pygame.HWSURFACE + pygame.SRCALPHA)
		self.bgcolor = Color(0,0,0,0);
		
		pygame.display.set_caption('ROUGELICK')
		self.font = pygame.font.SysFont(None,20)
		self.small_font = pygame.font.SysFont(None,20)
		self.GUI_ = GUI_environment.GUI(self.GUISurf,self.small_font)
		pygame.display.flip()

	def to_screen(self, drawing, destination):
		drawing.draw(destination)

	# OUTDATED DRAWING FUNCTIONS
	# MUST BE UPDATED WITH NEW GUI LOGIC

	def draw_alert(self, alert, color=const.GUI_WHT):
		# draws alert box
		self.alert = self.font.render(alert,True,color)
		self.GUISurf.blit(self.alert,(5,const.SCREEN_HEIGHT-100))
		pygame.display.flip()
		
		
	'''def draw_gold(self, gold_count):
		# renders gold
		self.GUISurf.blit(self.gold_screen, (750, 385))
		self.gold = self.small_font.render(str(gold_count), True, WHT, BLK)
		self.GUISurf.blit(self.gold, (800, 385))
		
	def draw_inventory(self, inventory=None):
		# renders inventory
		self.GUISurf.blit(self.inventory_screen, (750, 400))
		if inventory:
			items = inventory.get_items()
		else:
			items = []
		for i in range(items.__len__()):
			line = self.small_font.render('xxx', True, BLK, BLK)
			self.GUISurf.blit(line, (750, ((i+1)*15)+400))
		for item in items:
			line = self.small_font.render(item.title, True, WHT, BLK)
			self.GUISurf.blit(line, (750, (items.index(item)+1)*15+400))
		
	def draw_equipment(self, equipment=START_EQUIPMENT):
		# renders equipment. will change for more awesomeness
		self.GUISurf.blit(self.equipment_screen, (750, 200))
		for i in range(equipment.keys().__len__()):
			line = self.small_font.render('xxx', True, BLK, BLK)
			self.GUISurf.blit(line, (750, ((i+1)*15)+200))
		i = 1
		for slot in EQUIPMENT_TYPES:
			try:
				line_text = slot+': '+equipment[slot].title
			except:
				line_text = slot+': '
			line = self.small_font.render(line_text, True, WHT, BLK)
			self.GUISurf.blit(line, (750, i*15+200))
			i += 1'''
			
	def update(self):
		self.screen.blit(self.mapSurf, (0,0))
		self.screen.blit(self.spriteSurf, (0,0))
		self.screen.blit(self.GUISurf, (0,0))

	