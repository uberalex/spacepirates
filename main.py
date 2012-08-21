import pygame, sys

from renderer import GameCanvas
from engine import GameEngine

from pygame.locals import *

import random

pygame.init()

FPS = 5 

fpsClock = pygame.time.Clock()
canvas = GameCanvas()
gameengine = GameEngine()

while True:
    canvas.renderBoard(gameengine)
    canvas.renderShip(gameengine.ship)
    #move the ship about            
    gameengine.moveShip('Player',random.randint(0,7),random.randint(0,7))
    for event in pygame.event.get():
            if (event.type == KEYDOWN):
                pressed = pygame.key.name(event.key)
                print 'pressed ' + pressed
            elif event.type == QUIT:
                pygame.quit()
                sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)
