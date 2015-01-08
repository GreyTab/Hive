"""
Melissa Miranda
Jia Yang
mmirand2@binghamton.edu
jyang82@binghamton.edu
Final project
"""
'''
The Block class creates the basic building blocks to the game,
   which are then later customized

'''

# Imports
import pygame
from colors import *



class Block(pygame.sprite.Sprite):

    # -----------------------------------------------------------------------
    # Constructor
    def __init__(self, x, y,  width , height , color = black, blockType = 1):
        super(Block, self).__init__()
        self.image = pygame.Surface((width,height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        #self.originx = self.rect.centerx
        #self.originy = self.rect.centery
        self.rect.x = x #-self.originx
        self.rect.y = y #-self.originy
        self.blockType = blockType



    # -----------------------------------------------------------------------
    # Mutators
    def setImage(self, fileName = None):
        if fileName != None:
            self.image = pygame.image.load(fileName).convert()
