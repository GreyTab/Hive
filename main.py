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
				if event.type == pygame.QUIT :
					running = False
				player_logic.player_controls( event )

			# --------------------------------
			# Update positions and states
			clock.tick( FRAMERATE_CAP )
			handle_player_collision( player_logic, block_list )

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
	player_logic = Player(100,200)
	player_sprite = pygame.sprite.Group()
	player_sprite.add( player_logic )

	# block test (floor)
	block_list = pygame.sprite.Group()
	for x in range( 25 ) :
		block_list.add( Block( 0 + (32 * x), 500, 32, 100 ) )  # 32 x 100 blocks to create a "floor"

	return player_logic, player_sprite, block_list


def handle_player_collision( player_logic, object_list ) :

	for collidable in pygame.sprite.spritecollide( player_logic, object_list, False ) :
		if collidable.block_type == 1 :

			# collision at the top side of block
			if 	player_logic.rect.left < collidable.rect.right and \
					player_logic.rect.right > collidable.rect.left and \
					player_logic.rect.bottom >= collidable.rect.top :
						player_logic.rect.bottom = collidable.rect.top
						player_logic.v_vel = 0
						player_logic.in_air = False

			# collision at the right side of block
			if 	player_logic.rect.right < collidable.rect.left and \
					player_logic.rect.bottom > collidable.rect.top and \
					player_logic.rect.top < collidable.rect.bottom :
						player_logic.h_vel = 0

main()
