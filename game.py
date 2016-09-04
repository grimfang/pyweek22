#!/usr/bin/python

# Panda Engine imports
from panda3d.core import CardMaker, NodePath

# Game imports
from player import Player

#----------------------------------------------------------------------#

class Game():

    def __init__(self, _parent=None):
        self.parent = _parent

        # Physics world
        self.physics_world = None

        # Containers
        self.game_objects = {}
        self.game_doors = {}
        self.game_objects_np = render.attachNewNode("Game_Objects")
        self.game_doors_np = render.attachNewNode("Player_Doors")
        self.game_doors_np.setPos(0, 0, 0)

    def start(self):
    	self.loadLevel("assets/background.png", 5)

    	# player
    	self.loadPlayer("default")

    def stop(self):
    	pass

    def setPhysicsWorld(self, _physicsworld):
    	self.physics_world = _physicsworld

    #### LOADERS ####
    def loadLevel(self, _filename, z):
    	tex = loader.loadTexture(_filename)   
    	cm = CardMaker('Background')
    	sprite = NodePath(cm.generate())   
    	sprite.setTexture(tex)
    	sprite.setPos(-0.5, z, -0.5)

    	sprite.reparentTo(render)

    def loadPlayer(self, _name):
    	self.player = Player(self)
    	self.player.start()