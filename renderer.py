import pygame, sys

from pygame.locals import *

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
        self.DISPLAYSURF = pygame.display.set_mode( (500, 500), 0, 32)
        pygame.display.set_caption('Arr!')


    def renderBoard(self,board):
        self.DISPLAYSURF.fill(self.BLACK)
        #draw the border
        pygame.draw.line(self.DISPLAYSURF, self.WHITE, (50,50), (50,450), 2)
        pygame.draw.line(self.DISPLAYSURF, self.WHITE, (50,450), (450,450), 2)
        pygame.draw.line(self.DISPLAYSURF, self.WHITE, (450,450), (450,50), 2)
        pygame.draw.line(self.DISPLAYSURF, self.WHITE, (450,50), (50,50), 2)
        #calculate the board size
        for line in range(board.BOARDHEIGHT):
            for col in range(board.BOARDWIDTH):
                area = Rect(50*(col+1)+15,50*(line+1)+15,20,20)
                self.DISPLAYSURF.fill(self.GRAY, area)
    def renderShip(self,ship):
        xpos = ship.xpos + 1
        ypos = ship.ypos + 1
        triangle = [ (25 + (50 * xpos) , 15 + (50 * ypos) ),(15 + (50 * xpos) ,30 + (50 * ypos) ),(35 + (50 * xpos) ,30 + (50 * ypos) ) ]
        pygame.draw.polygon(self.DISPLAYSURF, self.RED, triangle, 0)
