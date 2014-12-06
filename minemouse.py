#!/usr/bin/env python2
import sys, datetime
sys.path.append("/opt/minecraft-pi/api/python/mcpi")
import minecraft
mc = minecraft.Minecraft.create()
mc.setting("world.immutable", True)
mc.setting("world.nametagsvisible", True)
def log(name, msg):
    mc.postToChat("[%s][%s] %s" % (datetime.datetime.now(), name, msg))
log("map", "Moving player...")
mc.player.setTilePos(0, 30, 15)
log("map", "Clearing...")
mc.setBlocks(-1, 10, -1, 33, 12, 33, 0)
log("map", "Generating base...")
mc.setBlocks(-1, 10, -1, 33, 10, 33, 1)
log("map", "Generating end...")
mc.setBlocks(15, 10, 15, 17, 10, 17, 41)
log("map", "Generating walls...")
mc.setBlocks(0, 11, 0, 0, 11, 32, 45)
mc.setBlocks(0, 11, 0, 32, 11, 0, 45)
mc.setBlocks(32, 11, 0, 32, 11, 32, 45)
mc.setBlocks(0, 11, 32, 32, 11, 32, 45)
log("map", "World ready for bot!")

class Bot(object):
    class Direction:
        NORTH = 0
        EAST = 1
        SOUTH = 2
        WEST = 3
        NAMES = {0:"north", 1:"east", 2:"south", 3:"west"}
    def __init__(self):
        self.log("Coming online")
        self.x = -5
        self.y = 11
        self.z = -5
        self.d = self.Direction.NORTH
        self.move(1, 1, self.Direction.NORTH)
    def log(self, msg):
        log("bot%i" % self.__hash__(), msg)
    def render(self, add=True):
        if add:
            mc.setBlock(self.x, self.y, self.z, 47)
            if self.d == self.Direction.NORTH:
                mc.setBlock(self.x+1, self.y+1, self.z, 20)
            if self.d == self.Direction.EAST:
                mc.setBlock(self.x, self.y+1, self.z+1, 20)
            if self.d == self.Direction.SOUTH:
                mc.setBlock(self.x-1, self.y+1, self.z, 20)
            if self.d == self.Direction.WEST:
                mc.setBlock(self.x, self.y+1, self.z-1, 20)
        else:
            mc.setBlock(self.x, self.y, self.z, 30)
            if self.d == self.Direction.NORTH:
                mc.setBlock(self.x+1, self.y+1, self.z, 0)
            if self.d == self.Direction.EAST:
                mc.setBlock(self.x, self.y+1, self.z+1, 0)
            if self.d == self.Direction.SOUTH:
                mc.setBlock(self.x-1, self.y+1, self.z, 0)
            if self.d == self.Direction.WEST:
                mc.setBlock(self.x, self.y+1, self.z-1, 0)
    def move(self, x, y, d):
        self.render(False)
        self.log("Heading %s to (%i;%i)" % (self.Direction.NAMES[d], x, y))
        self.x = x
        self.z = y
        self.d = d
        self.render(True)
    def scan(self, results):
        walls = ["I see %i walls" % (len(results))]
        if "north" in results:
            if results["north"] == 1:
                mc.setBlock(self.x+1, self.y, self.z, 44)
                walls.append("one to the north")
            else:
                mc.setBlock(self.x+1, self.y, self.z, 30)
        if "east" in results:
            if results["east"] == 1:
                mc.setBlock(self.x, self.y, self.z+1, 44)
                walls.append("one to the east")
            else:
                mc.setBlock(self.x, self.y, self.z+1, 30)
        if "south" in results:
            if results["south"] == 1:
                mc.setBlock(self.x-1, self.y, self.z, 44)
                walls.append("one to the south")
            else:
                mc.setBlock(self.x-1, self.y, self.z, 30)
        if "west" in results:
            if results["west"] == 1:
                mc.setBlock(self.x, self.y, self.z-1, 44)
                walls.append("one to the west")
            else:
                mc.setBlock(self.x, self.y, self.z-1, 30)
        self.log(", ".join(walls))
    def turn(self, d):
        self.log("Turning to the %s" % (self.Direction.NAMES[d]))
        self.render(False)
        self.d = d
        self.render(True)
    def forward(self, l=1):
        for i in range(0, l):
            if self.d == self.Direction.NORTH:
                self.move(self.x+1, self.z, self.d)
            if self.d == self.Direction.EAST:
                self.move(self.x, self.z+1, self.d)
            if self.d == self.Direction.SOUTH:
                self.move(self.x-1, self.z, self.d)
            if self.d == self.Direction.WEST:
                self.move(self.x, self.z-1, self.d)
    def go(self, d, l):
        while self.d != d:
            self.turn(d)
        self.forward(l)
