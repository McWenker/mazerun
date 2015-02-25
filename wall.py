import pygame
import constants as const

class Wall(pygame.sprite.Sprite):
	# WALL
	
	def __init__(self, left, top):
	
		# call parent
		super(Wall, self).__init__()
		
		# make blue wall
		self.image = pygame.Surface((const.TILE_SIZE, const.TILE_SIZE))
		self.image.fill((const.BRN))
		
		# set location
		self.rect = self.image.get_rect()
		self.rect.top = top
		self.rect.left = left