import pygame, sys

from pygame.locals import *
from pygame.sprite import Sprite

class ShipSprite():#Sprite):
    def __init__(self):#, color, initial_position):
        #superclass constructor
        #Sprite.__init__(self)

        
        #sprite's own canvas
        self.canvas = pygame.Surface([187,56])
        self.canvas.fill((128,128,255))

        self.shipImage = pygame.image.load('assets/images/rocket.png').convert()
        #self.shipImage.set_colorkey((self.shipImage.get_at([0,0])))

class GameCanvas:
    """Renders the game window"""   
    
    def __init__(self):
        #Set up some colour
        self.WHITE = (255,255,255)
        self.RED = (178,34,34)
        self.BLUE = (34,34,178)
        self.BLACK = (34,34,34)
        self.GRAY = (134,134,134)

        #screen geometry
        self.SCREENX = 1000
        self.SCREENY = 1000
        self.DISPLAYSURF = pygame.display.set_mode( (self.SCREENX+10, self.SCREENY+10), 0, 32)
        pygame.display.set_caption('Arr!')

        #load image assets
        self.nebulaBackground = pygame.image.load('assets/images/nebula.jpg').convert()
        self.shipSprite = ShipSprite()

        #mouse
        pygame.mouse.set_visible(False)


    def renderBoard(self,board):
        #self.DISPLAYSURF.fill(self.BLACK)
        self.DISPLAYSURF.blit(self.nebulaBackground, [0, 0])
        
        #draw the border
        pygame.draw.line(self.DISPLAYSURF, self.WHITE, (0,0), (0,self.SCREENY), 2)
        pygame.draw.line(self.DISPLAYSURF, self.WHITE, (0,self.SCREENY), (self.SCREENX,self.SCREENY), 2)
        pygame.draw.line(self.DISPLAYSURF, self.WHITE, (self.SCREENX,self.SCREENY), (self.SCREENX,0), 2)
        pygame.draw.line(self.DISPLAYSURF, self.WHITE, (self.SCREENX,0), (0,0), 2)

        #draw 10 pixel lines to represent the edges of the squares
        for y in range(1,board.BOARDHEIGHT):
            pygame.draw.line(self.DISPLAYSURF, self.GRAY, (0,y*100), (self.SCREENX, y*100), 2)

        for x in range(1,board.BOARDWIDTH):
            pygame.draw.line(self.DISPLAYSURF, self.GRAY, (x*100, 0), (x*100, self.SCREENY), 2)

    def renderPointer(self, coords):
        pygame.draw.line(self.DISPLAYSURF, self.BLUE, (coords[0]-15, coords[1]), (coords[0]+15, coords[1]), 4)
        pygame.draw.line(self.DISPLAYSURF, self.BLUE, (coords[0], coords[1]-15), (coords[0], coords[1]+15), 4)

    def renderShip(self,ship):
        #rects are (x,y,width,height)
        
        # jut draw an ellipse for the ship right now
        #shipRect = (ship.xpos-25,  ship.ypos-12.5, 50, 25)
        #pygame.draw.ellipse(self.DISPLAYSURF, self.RED, shipRect, 0)
        #draw the rotated ship
        rotated_surface = pygame.transform.rotate(self.shipSprite.shipImage, -1 * ship.vector[1])
        print rotated_surface.get_size()
        self.DISPLAYSURF.blit(rotated_surface, [ship.xpos-93.5, ship.ypos-28])
