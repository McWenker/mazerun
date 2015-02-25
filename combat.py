import pygame, random
from weapon import Weapon
from expreward import EXPReward
from treasure import Treasure
from constants import *

class Combat(object):
	# combat and damage handler

	def __init__(self, player, w_list, r_list, e_list, t_list, xp_list):

		self.weapon_type = 'ranged'

		self.player = player
		self.weapon_list = w_list
		self.wall_list = r_list
		self.enemy_list = e_list
		self.treasure_list = t_list

	def weaponAttack(self, evt, rect, nme, spd):
		if evt.key == pygame.K_w:
			weapon = Weapon('up',rect.centerx,rect.centery-10,nme,spd)
			weapon.attk(0,1)
			self.weapon_list.add(weapon)
		elif evt.key == pygame.K_a:
			weapon = Weapon('left',rect.centerx-10,rect.centery,nme,spd)
			weapon.attk(-1,0)
			self.weapon_list.add(weapon)
		elif evt.key == pygame.K_s:
			weapon = Weapon('down',rect.centerx,rect.centery,nme,spd)
			weapon.attk(0,-1)
			self.weapon_list.add(weapon)
		elif evt.key == pygame.K_d:
			weapon = Weapon('right',rect.centerx,rect.centery,nme,spd)
			weapon.attk(1,0)
			self.weapon_list.add(weapon)

	def weaponSelect(self):
		# allows swapping between weapons
		if self.weapon_type == 'ranged':
			self.weapon_type = 'melee'
		else:
			self.weapon_type = 'ranged'
	
	def weaponLogic(self, w):

		# collision?
		w.move()

		block_hit_list = pygame.sprite.spritecollide(w,
					self.wall_list, False)
		enemy_hit_list = pygame.sprite.spritecollide(w,
					self.enemy_list, False)
		# remove weapon
		for block in block_hit_list:
			self.weapon_list.remove(w)

		for enemy in enemy_hit_list:
			self.weapon_list.remove(w)
			# deal damage to enemy
			self.damageLogic(enemy, self.player,
					self.player.ranged_damage())
			
	def damageLogic(self, target, attacker, damage):
		# handles damage dealing
		target.take_damage(damage, attacker.rect.x,
				attacker.rect.y)
		if target.health <= 0:
			# if dead, removes from visual list
			self.enemy_list.remove(target)
			
			# rewards EXP to attacker
			# this function will need to be adjusted
			# to allow player-kill EXP rewards
			attacker.earn_EXP(target.EXP)

			self.lootRoll(target)

	def lootRoll(self, target):

		loot_roll = random.randint(0,30)
		# roll for loot
		if loot_roll > 15:
			loot = Treasure(target.rect.centerx, target.rect.centery)
			self.treasure_list.add(loot)
		# create EXP reward visual - MOVE TO VISUAL
		#xp_list.add(EXPReward(target.rect.centerx,
		#	target.rect.centery-TILE_SIZE, target.EXP))

	def swordLogic(self, s):

		# collision?
		enemy_hit_list = pygame.sprite.spritecollide(s,
					self.current_room.enemy_list, False)

		for enemy in enemy_hit_list:
			# deal damage to enemy
			if self.sword_count == 5:
				self.damageLogic(enemy, self.player,
						self.player.melee_damage())