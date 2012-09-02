import pygame, sys, math

from pygame.locals import *

class Ship:
    def __init__(self, name):
        self.name = name
        self.xpos = 500
        self.ypos = 500
        self.boardxpos = 0
        self.boardypos = 0
        #represent vector as direction, speed, where direction is angle degrees with up being 0. speed is number of squares per tick
        self.vector = [0,0]
    
    def moveShip(self, newx, newy):
        self.xpos = newx
        self.ypos = newy

    def deltaV(self, newspeed, newheading):
        self.vector = (newspeed, newheading)
    
    def changeHeading(self, heading):
        self.vector[1]  = (self.vector[1] + heading) % 360
        print 'changed heading by %s, new .vector %s, %s' % (heading, self.vector[0], self.vector[1])

    def changeSpeed(self, speed):
        self.vector[0] = (self.vector[0] + speed) % 50  if (self.vector[0] + speed) > 0 else 0
        
        print 'changed speed by %s, new .vector %s, %s' % (speed, self.vector[0], self.vector[1])
    
    def updatePos(self, width, height):
        self.xpos = (self.xpos + self.vector[0] * math.cos(math.radians(self.vector[1])) ) % width
        self.ypos = (self.ypos + self.vector[0] * math.sin(math.radians(self.vector[1])) ) % height

class GameEngine:
    """handles the back-end logic"""
    def __init__(self):
        #create 100 square board
        self.board = [0] * 100
        self.BOARDHEIGHT = 10
        self.BOARDWIDTH = 10
        #create the player ship
        #TODO:this should be refactored into a dictionary or linked list of ships to manage
        self.ship = Ship('Player')

    def moveShip(self, name, newx, newy):
        self.ship.move(newx, newy)
    
    def deltaVShip(self, name, speed, heading):
        self.ship.deltaV(speed,heading)

    def changeHeading(self, name, heading):
        self.ship.changeHeading(heading)

    def changeSpeed(self, name, speed):
        self.ship.changeSpeed(speed)

    def updateShip(self,name, width, height):
        self.ship.updatePos(width, height)
