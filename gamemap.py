import pygame
from room import Room

class GameMap(object):
	# map, for storing room objects and their attribs

	def get_rooms(self):
		rooms = []
	
		room = Room()
		rooms.append(room)
	
		room = Room()
		rooms.append(room)
	
		room = Room()
		rooms.append(room)
		return rooms