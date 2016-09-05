#!/usr/bin/python

# Panda Engine imports
from panda3d.core import CardMaker, NodePath

# Game imports
from player import Player
from builder import Builder

#----------------------------------------------------------------------#

class Game():

    def __init__(self, _parent=None):
        self.parent = _parent

        # Containers
        self.game_objects = {}
        self.game_doors = {}
        self.game_objects_np = render.attachNewNode("Game_Objects")
        self.game_doors_np = render.attachNewNode("Player_Doors")
        self.game_doors_np.setPos(0, 0, 0)

        # Physics world
        self.physics_world = None
        self.builder = Builder(self)

    def start(self):
    	self.loadLevel("assets/level0")

    	# player
    	self.loadPlayer("default")

    def stop(self):
    	pass

    def setPhysicsWorld(self, _physicsworld):
    	self.physics_world = _physicsworld

    #### LOADERS ####
    def loadLevel(self, _filename):
    	self.builder.parseEggFile(_filename)  
    	

    def loadPlayer(self, _name):
    	self.player = Player(self)
    	self.player.start()