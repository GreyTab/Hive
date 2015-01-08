"""
Melissa Miranda
Jia Yang
mmirand2@binghamton.edu
jyang82@binghamton.edu
Final project
"""
'''
Pygame GUI
Allows user to play a game in which the player controls a block that
  jumps whenever the user presses the up button on the keyboard
Tasks:
  Initialize pygame with
    Model -
      block (Block)
      player (Player)
      button (Screen)
'''
import pygame
from colors import *
from player import *
from block import *
from screen import *


# Constants
TWO = 2
THREE = 3
FOUR = 4
FIVE = 5
EIGHT = 8
TEN = 10
THIRTY_TWO = 32
FORTY = 40
SEVENTY_FIVE = 75
HUNDRED = 100
HUNDRED_FORTY = 140
FOUR_HUNDRED_EIGHTY = 480
SIX_HUNDRED = 600
SIX_HUNDRED_FORTY = 640


'''
The Level Class sets up the level of the game
'''
class Level(object):

    # ---------------------------------------------------------------------
    # Constructor
    def __init__(self, playerObject):
        self.platformList = pygame.sprite.Group()
        self.playerObject = playerObject
        self.playerStart = self.playerStartX, self.playerStartY = 0,0
        self.worldShiftX = self.worldShiftY = 0

        self.leftViewBox = windowWidth/TWO - windowWidth/EIGHT
        self.rightViewBox = windowWidth/TWO + windowWidth/TEN
        self.upViewBox = windowHeight/THREE #- windowHeight/EIGHT
        self.downViewBox = windowHeight - FORTY #+ windowHeight/EIGHT


    # -----------------------------------------------------------------------
    # Mutators
    def updateList(self):
        self.platformList.update()

    def draw(self, window):
        window.fill(silver)
        self.platformList.draw(window)

    def shiftWorld(self ,shiftX, shiftY):
        self.worldShiftX += shiftX
        self.worldShiftY += shiftY

        for object in self.platformList:
            object.rect.x += shiftX
            object.rect.y += shiftY

    def runViewBox(self):
        if self.playerObject.rect.x <= self.leftViewBox:
            viewDifference = self.leftViewBox - self.playerObject.rect.x
            self.playerObject.rect.x = self.leftViewBox
            self.shiftWorld( viewDifference ,0 )

        if self.playerObject.rect.x >= self.rightViewBox:
            viewDifference = self.rightViewBox - self.playerObject.rect.x
            self.playerObject.rect.x = self.rightViewBox
            self.shiftWorld( viewDifference ,0 )

        if self.playerObject.rect.y <= self.upViewBox:
            viewDifference = self.upViewBox - self.playerObject.rect.y
            self.playerObject.rect.y = self.upViewBox
            self.shiftWorld( 0 , viewDifference )

        if self.playerObject.rect.y >= self.downViewBox:
            viewDifference = self.downViewBox - self.playerObject.rect.y
            self.playerObject.rect.y = self.downViewBox
            self.shiftWorld( 0 , viewDifference )

    def createLevel(self,levelFileName = None):
        blockList = []
        x = y = 0

        if levelFileName != None:
            levelFile = open(levelFileName, 'r')
            for line in levelFile:
                for blockType in line:
                #blockType = line.split()
                    if blockType == '1':
                        #.setImage("img/ground.png")
                        platformBlock = [x, y, THIRTY_TWO, \
                                         THIRTY_TWO, black, 1]
                        blockList.append(platformBlock)
                    elif blockType == '2':
                        normalBlock = [x, y, THIRTY_TWO, THIRTY_TWO, \
                                       black, TWO]
                        blockList.append(normalBlock)
                    elif blockType == '3':
                        deathBlock = [x, y, THIRTY_TWO, THIRTY_TWO, \
                                      black, THREE]
                        blockList.append(deathBlock)
                    elif blockType == '4':
                        portalCube = [x, y, THIRTY_TWO, THIRTY_TWO, \
                                      black, FOUR]
                        blockList.append(portalCube)
                    x += THIRTY_TWO
                x = 0
                y += THIRTY_TWO
        return blockList
    
        """
        for block in blockList:
            block = Block( block[0], block [1], block [2],block[3], block[4])
            self.platformList.add(block)
        """




'''
The FirstLevel class sets up a specific level of the game
'''
class FirstLevel(Level):

    # ----------------------------------------------------------------------
    # Constructor
    def __init__(self, playerObject):
        super(FirstLevel,self).__init__(playerObject)
        level = Level(playerObject).createLevel("levels/level1.txt")

        """
        level = [ #x,y,width,height, color
        [-540,440, 4000, 40, black],
        [0,0,200, 20, black],
        [200,0, 32, 32, black]
        ]
        """
        for block in level:
            imageName = ""
            if block[FIVE] == 1:
                imageName = "img/ground.png"
            elif block[FIVE] == TWO:
                imageName = "img/brick.png"
            elif block[FIVE] == THREE:
                imageName = "img/deathCube.png"
            elif block[FIVE] == FOUR:
                imageName = "img/portal.png"

            block = Block( block[0], block [1], \
                           block [TWO],block[THREE], \
                           block[FOUR], block[FIVE])

            block.setImage(imageName)
            self.platformList.add(block)



# ----------------------------------------------------------------------------

# Main

pygame.init()

#creates the window
windowSize = windowWidth, windowHeight = SIX_HUNDRED_FORTY, \
             FOUR_HUNDRED_EIGHTY
window = pygame.display.set_mode( windowSize, pygame.RESIZABLE)
pygame.display.set_caption("Game")

window.fill( silver )

#frame rate per second, helps running program
clock = pygame.time.Clock()
fps = SEVENTY_FIVE

activeObjectList = pygame.sprite.Group()
player = Player()
player.setPosition(HUNDRED,HUNDRED_FORTY)
player.setImage('img/bighero6.png')
activeObjectList.add(player)
button = Screen() #makes quit button
button.setPosition(SIX_HUNDRED,0)
#button.button()
#button.setPosition(40,100)
activeObjectList.add(button)

levelList = []

levelList.append(FirstLevel(player))
#Level(player)
currentLevel = Level.createLevel("levels/level1.txt")
currentLevelNum = 0
currentLevel = levelList[currentLevelNum]
player.level = currentLevel





#fonts
#font =  pygame.font.SysFont('Arial', 90)
#text = font.render("Hello World", True, black)

#collidableObjects = pygame.sprite.Group()
#collidableObjects.add(secondBlock)
running = True
#event loop
while 1:
    for event in pygame.event.get():
        button.button()
    while running:
        for event in pygame.event.get():
            button.button()
            print(pygame.mouse.get_pressed())
            if (event.type == pygame.QUIT) or event.type == pygame.KEYDOWN \
                    and event.key == pygame.K_ESCAPE:
                running = False
            #Update Functions
        player.updatePosition(currentLevel.platformList, event)
        event  = None
        currentLevel.updateList()


            #Logic Testing
        currentLevel.runViewBox()

            #Draw everything
        currentLevel.draw(window)
        activeObjectList.draw(window)

            #Delay Framerate

        clock.tick(fps)

            #Update Screen
        pygame.display.update()

    pygame.quit()
