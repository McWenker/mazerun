import pygame, random

class LootTable(object):
	# rolls for loot
	def __init__(self, level):
		self.level = level

	def get_loot():	
		choice = random.randint(0,100)
		if choice < 20:
			self.item_type = 'coins'
			x = random.randint(1,30)
			self.count = x
			self.image = self.coin_image(self.count)			
		elif choice < 40:
			self.item_type = 'M. Weapon'
			self.title = 'Greatsword'
			self.m_damage = 5
			self.agi_buff = -1
			self.image = pygame.image.load(IMG_DIR + 'swadia.png')
		elif choice < 60:
			self.item_type = 'Hat'
			self.title = 'Iron Helm'
			self.armor = 2
			self.agi_buff = -1
			self.int_buff = -1
			self.image = pygame.image.load(IMG_DIR + 'helm.png')
		elif choice < 80:
			self.item_type = 'Hat'
			self.title = 'Fool\'s Crown'
			self.str_buff = 1
			self.int_buff = -1
			self.image = pygame.image.load(IMG_DIR + 'crown.png')
		elif choice <= 100:
			self.item_type = 'R. Weapon'
			self.title = 'Apprentice Wand'
			self.r_damage = 4
			self.str_buff = -1
			self.int_buff = 1
			self.image = pygame.image.load(IMG_DIR + 'wand.png')