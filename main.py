"""
	This file is responsible for combining game logic and
	loading content onto display
"""
import copy
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
	player_logic, player_sprite = init_player()
	block_list = init_level()

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


def init_player() :
	# player
	player_logic = Player(100,200)
	player_sprite = pygame.sprite.Group()
	player_sprite.add( player_logic )
	return player_logic, player_sprite


def init_level() :
	# block test (floor)
	block_list = pygame.sprite.Group()
	for x in range( 25 ) :
		block_list.add( Block( 0 + (32 * x), 500, 32, 100 ) )  # 32 x 100 blocks to create a "floor"

	# random block to jump on
	# block_list.add( Block( 368, 468, 32, 32 ) )
	block_list.add( Block( 368, 390, 32, 64 ) )

	return block_list


def handle_player_collision( player_logic, object_list ) :
	collision_list = pygame.sprite.spritecollide( player_logic, object_list, False )
	for collided_object in collision_list :
		inter_left = max( player_logic.rect.left, collided_object.rect.left )
		inter_right = min( player_logic.rect.right, collided_object.rect.right )
		inter_top = max( player_logic.rect.top, collided_object.rect.top )
		inter_bottom = min( player_logic.rect.bottom, collided_object.rect.bottom )
		inter_width = inter_right - inter_left
		inter_height = inter_bottom - inter_top

		if inter_width > 0 and inter_height > 0 :

			# top/bottom collision detection
			if inter_width > ( inter_height - abs( player_logic.v_vel ) ) :

				# falling down
				if player_logic.v_vel > 0 :
					player_logic.rect.bottom = collided_object.rect.top
					player_logic.on_ground = True

				# jumping up
				elif player_logic.v_vel < 0  :
					player_logic.rect.top += inter_height

				# stop further vertical movement
				player_logic.v_vel = 0

			# left/right collision
			if ( inter_height - abs( player_logic.v_vel ) ) > inter_width :

				# moving right
				if player_logic.h_vel > 0 :
					player_logic.rect.right = collided_object.rect.left

				# moving left
				elif player_logic.h_vel < 0:
					player_logic.rect.left = collided_object.rect.right

				# stop further horizontal movement
				player_logic.h_vel = 0

	# check that, in the next update, the player will still be on the ground
	if player_logic.v_vel == 0 and player_logic.on_ground :
		next_pos = copy.deepcopy( player_logic )
		next_pos.rect.bottom += 1
		player_logic.on_ground = len( pygame.sprite.spritecollide( next_pos, object_list, False ) ) != 0






main()
