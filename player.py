"""
Melissa Miranda
Jia Yang
mmirand2@binghamton.edu
jyang82@binghamton.edu
Final project
"""
'''
The Player class creates the player controlled block
'''

# Imports
import pygame
from colors import *

# CONSTANTS
POINT_THIRTY_FIVE = .35
TWO = 2
THREE = 3
FOUR = 4
FIVE = 5
THIRTY_TWO = 32


class Player( pygame.sprite.Sprite):

    # -----------------------------------------------------------------------
    # Constructor
    
    #initializes the Block class, creates the block
    def __init__(self, color = pink, width = THIRTY_TWO, height = THIRTY_TWO):
        super(Player, self).__init__()
        self.image = pygame.Surface((width,height))
        self.image.fill(color)

        self.setProperties()
        self.heightSpeed = 1
        self.horizontalSpeed = 0

        self.level = None


    # ----------------------------------------------------------------------
    # Mutators

    #sets properties of the block
    def setProperties(self):
        self.rect = self.image.get_rect()
        self.originx = self.rect.centerx
        self.originy = self.rect.centery
        self.speed = FIVE

    #changes the speed of the block/allows movement
    def changeSpeed(self, heightSpeed, horizontalSpeed):
        self.heightSpeed = heightSpeed
        self.horizontalSpeed += horizontalSpeed

    #sets postion of block
    def setPosition(self, x ,y):
        #self.rect = self.image.get_rect()
        self.rect.x = x - self.originx
        self.rect.y = y - self.originy


    #sets image from an image in a file
    def setImage(self, fileName = None):
        if fileName != None:
            self.image = pygame.image.load(fileName).convert()

    #updates blocks, includes collision
    def updatePosition(self, collidable = pygame.sprite.Group(), event = None):
        self.rect.x +=  TWO #self.heightSpeed
        self.experienceGravity()
        collisionList = pygame.sprite.spritecollide(self, collidable, False)

        for collidedObject in collisionList:
            if collidedObject.blockType == TWO or \
               collidedObject.blockType == THREE:
                pygame.quit()
                quit()
                print("Touch me, gently.")
            if self.heightSpeed > 0: #right direction
                if self.rect.bottom >= collidedObject.rect.top:
                    self.heightSpeed = 1
                self.rect.right = collidedObject.rect.left
            elif self.heightSpeed < 0: #left direction
                self.rect.left = collidedObject.rect.right

        self.rect.y += self.horizontalSpeed #-3 # subtract = higher jumos

        collisionList = pygame.sprite.spritecollide(self, collidable, False)

        for collidedObject in collisionList:
            if collidedObject.blockType == THREE or \
               collidedObject.blockType == FOUR:
                print("rekt")
                pygame.quit()
                quit()
            if self.horizontalSpeed > 0: #down direction
                self.rect.bottom = collidedObject.rect.top

                self.horizontalSpeed = 0

            elif self.horizontalSpeed < 0: #up direction
                self.rect.top = collidedObject.rect.bottom
                self.horizontalSpeed = 0



        self.changeSpeed(1, 0) #moves player to the right at constant speed
        if not(event == None):
            if event.type == pygame.KEYDOWN:
                #if event.key == pygame.K_LEFT:
                    #self.changeSpeed(-(self.speed), 0)
                #if event.key == pygame.K_RIGHT:
                   # self.changeSpeed((self.speed), 0)
                if event.key == pygame.K_UP:
                    if self.horizontalSpeed == 0:
                        self.changeSpeed( 1 , -(self.speed)*TWO)
                if event.key == pygame.K_DOWN:
                    pass
                    #self.changeSpeed( 0, 5)
            if event.type == pygame.KEYUP:
                #if event.key == pygame.K_LEFT:
                   # if self.heightSpeed != 0: self.heightSpeed = 0
                #if event.key == pygame.K_RIGHT:
                  # if self.heightSpeed != 0: self.heightSpeed = 0
                if event.key == pygame.K_UP:
                    if self.horizontalSpeed  != 0: self.horizontalSpeed = FOUR
                    #pass
                if event.key == pygame.K_DOWN:
                    pass
                    #if self.horizontalSpeed != 0: self.verticalSpeed = 0
                
    def experienceGravity(self , gravity = POINT_THIRTY_FIVE):
        if self.horizontalSpeed == 0:
            self.horizontalSpeed = FIVE
        else:
            self.horizontalSpeed += gravity
