"""
The Player class creates the player controlled block
"""
import pygame

GRAVITY = 3
PLAYER_SPEED = 4
DEFAULT_WIDTH_32 = 32
DEFAULT_HEIGHT_32 = 32
DEFAULT_COLOR_PINK = (255, 200, 210)


class Player( pygame.sprite.Sprite ) :
	# -----------------------------------------------------------------------
	# Constructor
	def __init__( self, x, y, width=DEFAULT_WIDTH_32, height=DEFAULT_HEIGHT_32, color=DEFAULT_COLOR_PINK ) :
		super( Player, self ).__init__()
		self.image = pygame.Surface( (width, height) )
		self.image.fill( color )

		# Positioning
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.originx = self.rect.centerx
		self.originy = self.rect.centery

		# Velocity
		self.h_vel = 0
		self.v_vel = 0

		# Jumping variable
		self.in_air = True

	# ----------------------------------------------------------------------
	# Mutators

	# changes the velocity of the block/allows movement
	def set_vel( self,  h_vel, v_vel ) :
		self.h_vel = h_vel
		self.v_vel = v_vel

	# sets postion of block
	def set_pos( self, x, y ) :
		self.rect.x = x
		self.rect.y = y

	# sets image from an image in a file
	def set_image( self, filename ) :
		self.image = pygame.image.load( filename ).convert()

	# updates position of the block based on velocity
	def update(self):
		self.rect.x += self.h_vel
		self.rect.y += self.v_vel

		# experience gravity
		# if self.in_air :
		# 	self.v_vel += GRAVITY

	# set controls for the player class, given an event
	def player_controls( self, event ) :
		if event is not None :
			if event.type == pygame.KEYDOWN :
				if event.key == pygame.K_LEFT:
					self.h_vel = -PLAYER_SPEED
				if event.key == pygame.K_RIGHT:
					self.h_vel = PLAYER_SPEED
				if event.key == pygame.K_UP:
					self.v_vel = -PLAYER_SPEED
				if event.key == pygame.K_DOWN:
					self.v_vel = PLAYER_SPEED

			if event.type == pygame.KEYUP :
				if event.key == pygame.K_LEFT:
					self.h_vel = 0
				if event.key == pygame.K_RIGHT:
					self.h_vel = 0
				if event.key == pygame.K_UP:
					self.v_vel = 0
				if event.key == pygame.K_DOWN:
					self.v_vel = 0