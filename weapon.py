import pygame, random
import constants as const

class Weapon(pygame.sprite.Sprite):
	# BULLET BILL/SWADIAN SWAD
	def __init__(self, shape, x, y, name, speed):
		# call parent
		super(Weapon, self).__init__()

		self.shape = shape
		self.name = name
		self.image = self.get_shape(self.shape)
		self.speed = speed

		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

	def get_shape(self, shape):
		return pygame.image.load(const.IMG_DIR+self.name+' '+shape+'.png')
		

	def move(self):
		if self.x_bool > 0:
			self.rect.x += self.speed
		if self.x_bool < 0:
			self.rect.x -= self.speed
		if self.y_bool > 0:
			self.rect.y -= self.speed
		if self.y_bool < 0:
			self.rect.y += self.speed

	def attk(self, x_bool, y_bool):
		self.x_bool = x_bool
		self.y_bool = y_bool