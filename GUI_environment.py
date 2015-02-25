import pygame
import visual_ele as GUI_env
import constants as const

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
	
	def __init__(self, surface, font):
		SceneBase.__init__(self)
		self.surface = surface
		self.font = font
		self.gui_BackG = pygame.sprite.Group()
		self.gui_Action_list = pygame.sprite.Group()
		self.gui_Hero_list = pygame.sprite.Group()
		self.misc_list = pygame.sprite.Group()

		# GUI background
		self.bottom_bar = GUI_env.VisualElement(0,const.SCREEN_HEIGHT-80,
			const.SCREEN_WIDTH,80,(const.GUI_WHT))
		self.left_bar = GUI_env.VisualElement(0,0,5,const.SCREEN_HEIGHT,
			(const.GUI_WHT))
		self.right_bar = GUI_env.VisualElement(const.SCREEN_WIDTH-5,0,5,
			const.SCREEN_HEIGHT,(const.GUI_WHT))
		self.top_bar = GUI_env.VisualElement(0,0,const.SCREEN_WIDTH,5,
			(const.GUI_WHT))

		# actionbar squares
		self.action_square1 = GUI_env.ClickableElement(5,const.SCREEN_HEIGHT-75,
			70,70,(const.GUI_RED))
		self.action_square2 = GUI_env.ClickableElement(80,const.SCREEN_HEIGHT-75,
			70,70,(const.GUI_RED))
		self.action_square3 = GUI_env.ClickableElement(155,const.SCREEN_HEIGHT-75,
			70,70,(const.GUI_RED))
		self.action_square4 = GUI_env.ClickableElement(230,const.SCREEN_HEIGHT-75,
			70,70,(const.GUI_RED))
		self.action_square5 = GUI_env.ClickableElement(305,const.SCREEN_HEIGHT-75,
			70,70,(const.GUI_RED))

		# hero/levelup squares
		self.hero_class1 = GUI_env.ClickableElement(380,const.SCREEN_HEIGHT-75,
			25,25,(const.GUI_YEL))
		self.hero_class2 = GUI_env.ClickableElement(410,const.SCREEN_HEIGHT-75,
			25,25,(const.GUI_YEL))
		self.hero_class3 = GUI_env.ClickableElement(440,const.SCREEN_HEIGHT-75,
			25,25,(const.GUI_YEL))

		# miscellaneous squares
		self.menu_button = GUI_env.ClickableElement(380,const.SCREEN_HEIGHT-45,
			85,40,(const.GUI_GRN))
		self.hero_button = GUI_env.ClickableElement(470,const.SCREEN_HEIGHT-75,
			70,70,(const.GUI_BLK))

		# lists to hold GUI windows
		self.gui_BackG.add(self.bottom_bar,self.top_bar,self.left_bar,self.right_bar)
		self.gui_Action_list.add(self.action_square1,self.action_square2,self.action_square3,
			self.action_square4,self.action_square5)
		self.gui_Hero_list.add(self.hero_class1,self.hero_class2,self.hero_class3)
		self.misc_list.add(self.menu_button,self.hero_button)
		
	def process_input(self):
		# checks for input on GUI buttons
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				self.button_logic()
			if event.type == pygame.QUIT:
				self.terminate()
				
	def button_logic(self):
		# determines what to do based on what button
		# will need further expansion to handle specific buttons

		# action button pressed?
		for AB in self.gui_Action_list:
			if AB.rect.collidepoint(pygame.mouse.get_pos()):
				pass
		# hero button pressed?
		for HB in self.gui_Hero_list:
			if HB.rect.collidepoint(pygame.mouse.get_pos()):
				pass
		# misc button pressed
		for MB in self.misc_list:
			if MB.rect.collidepoint(pygame.mouse.get_pos()):
				pass

	def update(self):
		# previously used to update GUI state
		pass

	def draw_stats(self,player_stats,color=const.GUI_BLK):
		# renders player stats
		# player name
		self.stats_screen = self.font.render(player_stats.name,True,
			color,const.GUI_WHT)
		self.surface.blit(self.stats_screen,(545,const.SCREEN_HEIGHT-77))

		# player level		
		self.stats_screen = self.font.render('Level: {}'.format(
			player_stats.level),True,color,const.GUI_WHT)
		self.surface.blit(self.stats_screen,(545,const.SCREEN_HEIGHT-61))

		# player XP
		self.stats_screen = self.font.render('EXP: {}'.format(
			player_stats.EXP),True,color,const.GUI_WHT)
		self.surface.blit(self.stats_screen,(545,const.SCREEN_HEIGHT-45))

		# player HP
		self.stats_screen = self.font.render('HP: {}/{}'.format(
			(player_stats.current_hp),(player_stats.max_hp)),True,color,
			const.GUI_WHT)
		self.surface.blit(self.stats_screen,(545,const.SCREEN_HEIGHT-29))

		# melee damage
		self.stats_screen = self.font.render('M. Damage: {}'.format(
			player_stats.melee_damage()),True,color,const.GUI_WHT)
		self.surface.blit(self.stats_screen,(655,const.SCREEN_HEIGHT-77))

		# ranged damage
		self.stats_screen = self.font.render('R. Damage: {}'.format(
			player_stats.ranged_damage()),True,color,const.GUI_WHT)
		self.surface.blit(self.stats_screen,(655,const.SCREEN_HEIGHT-61))

		# armor
		self.stats_screen = self.font.render('Armor: {}'.format(
			player_stats.armor()),True,color,const.GUI_WHT)
		self.surface.blit(self.stats_screen,(655,const.SCREEN_HEIGHT-45))

		# secondary stats and gold
		line = const.SCREEN_HEIGHT-77
		for stat in const.STATS:
			if hasattr(player_stats,stat):
				s = str(getattr(player_stats,stat))
			else:
				s = str(player_stats.stats[stat])
				
				self.stats_screen = self.font.render('{}: {}'.format(
					stat, s),True,color,const.GUI_WHT)
				self.surface.blit(self.stats_screen,(765, line))
				line += 16
		
	def render(self):
		# draws GUI based on current state
		# should be moved to screen logic
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