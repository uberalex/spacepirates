import pygame, sys

from renderer import GameCanvas
from engine import GameEngine

from pygame.locals import *

import random

pygame.init()

FPS =  60

fpsClock = pygame.time.Clock()
canvas = GameCanvas()
gameengine = GameEngine()

#walk the ship across the board
#gameengine.deltaVShip('Player', 1, 45)

while True:
    canvas.renderBoard(gameengine)
    canvas.renderShip(gameengine.ship)
    canvas.renderPointer(pygame.mouse.get_pos())
    
    #move the ship about at rangom
    #gameengine.moveShip('Player',random.randint(0,7),random.randint(0,7))
    
    gameengine.updateShip('Player', canvas.SCREENX, canvas.SCREENY)

    for event in pygame.event.get():
            if (event.type == KEYDOWN):
                pressed = pygame.key.name(event.key)
                if pressed == 'left':
                    gameengine.changeHeading('Player1',-5)
                elif pressed == 'right':
                    gameengine.changeHeading('Player1',5)
                elif pressed == 'up':
                    gameengine.changeSpeed('Player1',15)
                elif pressed == 'down':
                    gameengine.changeSpeed('Player1',-5)

            elif event.type == QUIT:
                pygame.quit()
                sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)
