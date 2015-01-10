"""
	This file is responsible for combining game logic and
	loading content onto display
"""
import pygame
from block import Block
from player import Player

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FRAMERATE_CAP = 60
BACKGROUND_COLOR = (105, 192, 255)  # skyblue color


def main() :
	pygame.init()
	pygame.display.set_caption( "Game" )
	window = pygame.display.set_mode( (WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE )

	# initialize player and level OUTSIDE of main game loop
	player_logic, player_sprite, block_list = init_player_and_blocks()

	running = True
	clock = pygame.time.Clock()
	try :
		while running :
			# continue to draw background to prevent sprite trails
			window.fill( BACKGROUND_COLOR )

			# --------------------------------
			# Event handling
			for event in pygame.event.get() :
				player_logic.player_controls( event )
				if event.type == pygame.QUIT :
					running = False

			# --------------------------------
			# Update positions and states
			clock.tick( FRAMERATE_CAP )

			player_logic.update()
			player_sprite.draw( window )
			block_list.draw( window )

			pygame.display.update()

		# ----------------------------------
		# Exiting
		pygame.display.quit()
		pygame.quit()

	except SystemExit :
		pygame.display.quit()
		pygame.quit()


def init_player_and_blocks() :
	# player
	player_logic = Player(100,100)
	player_sprite = pygame.sprite.Group()
	player_sprite.add( player_logic )

	# block test (floor)
	block_list = pygame.sprite.Group()
	for x in range( 25 ) :
		block_list.add( Block( 0 + (32 * x), 500, 32, 100 ) )  # 32 x 100 blocks to create a "floor"

	return player_logic, player_sprite, block_list


main()
