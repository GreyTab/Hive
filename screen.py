"""
Melissa Miranda
Jia Yang
mmirand2@binghamton.edu
jyang82@binghamton.edu
Final project
"""
'''
The Screen class creates the screen in which the game exists
'''


# Imports
import pygame
from colors import *


# CONSTANTS
TWO = 2
THIRTY = 30
FIFTY = 50


class Screen(pygame.sprite.Sprite):

    # --------------------------------------------------------------------
    # Constructor
    def __init__(self,color = pink,buttonWidth = FIFTY, buttonHeight = THIRTY):
        super(Screen, self).__init__()
        self.image = pygame.Surface((buttonWidth,buttonHeight))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        #self.originx = self.rect.centerx
        #self.originy = self.rect.centery
        #self.rect.x = buttonX #-self.originx
        #self.rect.y = buttonY #-self.originy
        #self.blockType = blockType


    # --------------------------------------------------------------------
    # Mutators
    def setProperties(self):
        self.rect = self.image.get_rect()
        self.originx = self.rect.centerx
        self.originy = self.rect.centery

        
    def setPosition(self, x ,y):
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y



        #self.click = pygame.mouse.get_pressed()
        #self.image = pygame.Surface((buttonWidth,buttonHeight))
       # self.image.fill(color)

    def button(self, action = None):
        self.mouse = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()
        if self.rect.x + FIFTY > self.mouse[0] > self.rect.x and \
           self.rect.y + THIRTY > self.mouse[1] > self.rect.y:
            self.image.fill(black)
              # print("touched")
            if self.click[0] == 1 :
                pygame.init()
            elif self.click[TWO] ==1 :
                pygame.quit()
                quit()
        else:
            self.image.fill(pink)
    #def getMouse(self):

