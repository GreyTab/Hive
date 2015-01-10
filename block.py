"""
	Levels are generated as blocks of various types
"""
import pygame

TYPE_ONE_BLACK = (20, 25, 55)


class Block( pygame.sprite.Sprite ) :
	# -----------------------------------------------------------------------
	# Constructor
	def __init__( self, x, y, width, height, color=TYPE_ONE_BLACK, block_type=1 ) :
		super( Block, self ).__init__( )

		self.image = pygame.Surface( (width, height) )
		self.image.fill( color )
		self.rect = self.image.get_rect( )
		# self.originx = self.rect.centerx
		# self.originy = self.rect.centery
		self.rect.x = x  # -self.originx
		self.rect.y = y  # -self.originy
		self.block_type = block_type

	# -----------------------------------------------------------------------
	# Mutators
	def set_image( self, filename ) :
		self.image = pygame.image.load( filename ).convert( )
