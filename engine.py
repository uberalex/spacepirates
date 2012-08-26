import pygame, sys, math

from pygame.locals import *

class Ship:
    def __init__(self, name):
        self.name = name
        self.xpos = 0
        self.ypos = 0
        #represent vector as direction, speed, where direction is angle degrees with up being 0. speed is number of squares per tick
        self.vector = (0,0)
    
    def moveShip(self, newx, newy):
        self.xpos = newx
        self.ypos = newy

    def deltaV(self, newspeed, newheading):
        self.vector = (newspeed, newheading)

    def updatePos(self, width, height):
        self.xpos = (self.xpos + self.vector[0] * math.cos(math.radians(self.vector[1])) ) % width
        self.ypos = (self.ypos + self.vector[0] * math.sin(math.radians(self.vector[1])) ) % height

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
    
    def deltaVShip(self, name, speed, heading):
        self.ship.deltaV(speed,heading)

    def updateShip(self,name):
        self.ship.updatePos(self.BOARDWIDTH, self.BOARDHEIGHT)
