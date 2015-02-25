import pygame, sys
from pygame.locals import *

sys.path.append('roguey\classes')

from game import Game

def main():
	while 1:
		pygame.init()
		game = Game()

if __name__ == '__main__':
	main()
