import pygame, random, sys
import constants as const
from gamemap import GameMap
from room import Room
from wall import Wall
from player import Player
from inventory import Inventory
from weapon import Weapon
from screen import Screen
from enemy import Enemy
from treasure import Treasure
from expreward import EXPReward
from combat import Combat

class Game(object):
	## MAIN GAME CLASS
	def __init__(self):
		# init pygame and abstract classes
		self.clock = pygame.time.Clock()
		self.screen = Screen()
		self.gamemap = GameMap()

		# init game state
		self.game_state = 'PREPARING'
	
		# create player paddle and inventory
		self.player = Player(100, 50, 50)
		self.inventory = Inventory()

		# create sprite Groups for game logic
		self.player_list = pygame.sprite.Group()
		self.weapon_list = pygame.sprite.Group()
		self.expReward_list = pygame.sprite.Group()

		self.player_list.add(self.player)	

		# sword swing int
		self.sword_count = 0
	
		# invulnerability timer
		self.invuln_count = 0
		
		# create rooms
		# there has to be a better way
		self.rooms = self.gamemap.get_rooms()
		
		self.current_room_num = 0
		self.current_room = self.rooms[self.current_room_num]

		# define default weapon type
		self.combat = Combat(self.player,self.weapon_list,self.current_room.wall_list,
			self.current_room.enemy_list, self.current_room.treasure_list, self.expReward_list)
		
		self.run()

	def terminate(self):
		pygame.quit()
		sys.exit()

	def run(self):
		self.screen.to_screen(self.current_room.wall_list, self.screen.mapSurf)

		self.game_state = 'RUNNING'	
		while 1:		
			self.clock.tick(60)
			# event processing
		
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.terminate()
			
				if event.type == pygame.KEYDOWN:
					self.keyboardDown(event)
						
				if event.type == pygame.KEYUP:
					self.keyboardUp(event)
					
			# game logic

			if self.game_state == 'RUNNING':
		
				self.gameplay_modelUpdate()
				self.gameplay_viewerUpdate(self.screen)
			
		pygame.quit()

	def add_treasure(self, treasure):
		text = 'You found %s. %s' % (treasure.title, treasure.desc)
		self.inventory.add_to_inventory(treasure, self.player)
		self.screen.draw_alert(text)
		
	def keyboardDown(self, evt):
		if evt.key == pygame.K_ESCAPE:
			self.doMenu()
		if self.game_state == 'RUNNING':
			if evt.key == pygame.K_LCTRL:
				self.combat.weaponSelect()
			if evt.key == pygame.K_LEFT:
				self.player.change_speed(-5, 0)
			if evt.key == pygame.K_RIGHT:
				self.player.change_speed(5, 0)
			if evt.key == pygame.K_UP:
				self.player.change_speed(0, -5)
			if evt.key == pygame.K_DOWN:
				self.player.change_speed(0, 5)
			
			if self.combat.weapon_type == 'ranged':
				self.combat.weaponAttack(evt,self.player.rect,'arrah',3)
				
			if self.combat.weapon_type == 'melee':
				self.combat.weaponAttack(evt,self.player.rect,'swadia',40)

	def doMenu(self):
		if self.game_state == 'RUNNING':
			self.game_state = 'PAUSED'
		else: self.game_state = 'RUNNING'
					
	def keyboardUp(self, evt):
		if evt.key == pygame.K_LEFT:
			self.player.change_speed(5, 0)
		if evt.key == pygame.K_RIGHT:
			self.player.change_speed(-5, 0)
		if evt.key == pygame.K_UP:
			self.player.change_speed(0, 5)
		if evt.key == pygame.K_DOWN:
			self.player.change_speed(0, -5)
			
	def gameplay_modelUpdate(self):
		self.player.move(self.current_room.wall_list)

		for w in self.weapon_list:
			self.combat.weaponLogic(w)
			
		for m in self.current_room.enemy_list:
			self.monsterLogic(m)

		for l in self.current_room.treasure_list:
			self.lootLogic(l)

		for r in self.expReward_list:
			r.counter -= 1
			if r.counter == 0:
				self.expReward_list.remove(r)
	
	
	def swingSword(self, evt):
		if evt.key == pygame.K_w:
			sword = Weapon('up',self.player.rect.centerx,
						self.player.rect.centery-50,'swadia',40)
			sword.attk(0,1)
			self.sword_count = 5
			self.sword_list.add(sword)
		elif evt.key == pygame.K_a:
			sword = Weapon('left',self.player.rect.centerx-55,
						self.player.rect.centery,'swadia',40)
			sword.attk(-1,0)
			self.sword_count = 5
			self.sword_list.add(sword)
		elif evt.key == pygame.K_s:
			sword = Weapon('down',self.player.rect.centerx,
						self.player.rect.centery+6,'swadia',40)
			sword.attk(0,-1)
			self.sword_count = 5
			self.sword_list.add(sword)
		elif evt.key == pygame.K_d:
			sword = Weapon('right',self.player.rect.centerx+6,
						self.player.rect.centery,'swadia',40)
			sword.attk(1,0)
			self.sword_count = 5
			self.sword_list.add(sword)
	
	def gameplay_viewerUpdate(self, screen):
		# updates visual elements
		screen.screen.fill(const.BLK)
		
		screen.spriteSurf.fill(screen.bgcolor);
		screen.GUISurf.fill(screen.bgcolor);


		if self.game_state == 'RUNNING':	
			screen.to_screen(self.current_room.enemy_list,screen.spriteSurf)
			screen.to_screen(self.current_room.treasure_list,screen.spriteSurf)
			screen.to_screen(self.expReward_list,screen.spriteSurf)
			screen.to_screen(self.weapon_list,screen.spriteSurf)
			screen.to_screen(self.player_list,screen.spriteSurf)
			screen.GUI_.render()			
			screen.GUI_.draw_stats(self.player)

		
		screen.update()
			
		pygame.display.flip()

	def monsterLogic(self, m):
	
		m.move(self.current_room.wall_list)
		enemy_hit_player = pygame.sprite.spritecollide(self.player,
								self.current_room.enemy_list,False)

		for enemy in enemy_hit_player:
			# deal damage to player
			if self.invuln_count == 0:
				self.player.take_damage(enemy.damage,enemy.rect.x,enemy.rect.y)
				self.invuln_count = 1000
				if self.player.health <= 0:
					pass
			else:
				self.invuln_count -= 1
	
	def lootLogic(self, l):
		treasure_picked_up = pygame.sprite.spritecollide(self.player,
						self.current_room.treasure_list,True)

		for treasure in treasure_picked_up:
			# pick up loot!
			self.add_treasure(treasure)
	
if __name__ == "__main__":
	main()