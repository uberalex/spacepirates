import pygame, sys

from renderer import GameCanvas
from engine import GameEngine

from pygame.locals import *

import random

pygame.init()

FPS = 30 

fpsClock = pygame.time.Clock()
canvas = GameCanvas()
gameengine = GameEngine()

#walk the ship across the board
gameengine.deltaVShip('Player', 1, 30)

while True:
    canvas.renderBoard(gameengine)
    canvas.renderShip(gameengine.ship)
    canvas.renderPointer(pygame.mouse.get_pos())
    
    #move the ship about at rangom
    #gameengine.moveShip('Player',random.randint(0,7),random.randint(0,7))
    
    gameengine.updateShip('Player')

    for event in pygame.event.get():
            if (event.type == KEYDOWN):
                pressed = pygame.key.name(event.key)
                print 'pressed ' + pressed
            elif event.type == QUIT:
                pygame.quit()
                sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)
