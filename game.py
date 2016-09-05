#!/usr/bin/python

# Panda Engine imports
from panda3d.core import CardMaker, NodePath, DirectionalLight

# Game imports
from player import Player
from builder import Builder
from dude import Dude

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

        # level lights
        self.directLight = None

    def start(self):
        self.loadLevel("assets/level0")
        self.loadLights()
        # player
        self.loadPlayer("default")
        self.loadDude()

    def stop(self):
    	#self.player.stop()
    	#self.dude.stop()
    	#self.physics_world = None

    	render.clearLight(self.directLight)
    	self.directLight = None

    def setPhysicsWorld(self, _physicsworld):
    	self.physics_world = _physicsworld

    #### LOADERS ####
    def loadLevel(self, _filename):
        self.builder.parseEggFile(_filename)


    def loadLights(self):
        # Set a simple light
        dlight = DirectionalLight('DirectLight')
        dlnp = render.attachNewNode(dlight)
        dlnp.setHpr(-30, 0, 0)
        render.setLight(dlnp)
        self.directLight = dlnp

    def loadPlayer(self, _name):
        self.player = Player(self)
        self.player.start()

    def loadDude(self):
        self.dude = Dude(self)
        self.dude.start()