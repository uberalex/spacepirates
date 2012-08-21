import pygame, sys

from pygame.locals import *

class Ship:
    def __init__(self, name):
        self.name = name
        self.xpos = 1
        self.ypos = 1
        #represent vector as direction, speed, where direction is 0-7 direction counted clockwise with up being 0. speed is number of squares per tick
        self.vector = (0,0)
    def move(self, newx, newy):
        self.xpos = newx
        self.ypos = newy

class GameEngine:
    """handles the back-end logic"""
    def __init__(self):
        #create 64 square board
        self.board = [0] * 64
        self.BOARDHEIGHT = 8
        self.BOARDWIDTH = 8
        #create the player ship
        #TODO:this should be refactored into a dictionary or linked list of ships to manage
        self.ship = Ship('Player')
    def moveShip(self, name, newx, newy):
        self.ship.move(newx, newy)

