#!/usr/bin/python

# Panda Engine imports
from panda3d.core import CardMaker, NodePath, DirectionalLight
from direct.task.Task import Task

# Game imports
from player import Player
from builder import Builder
from dude import Dude
from hud import Hud

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
        self.game_counter_node = None

        self.redDudesCount = 0
        self.blueDudesCount = 0
        self.isLosing = False

        # Physics world
        self.physics_world = None
        self.builder = Builder(self)

        # level lights
        self.directLight = None

        # Dude class
        self.dude = None
        self.spawnPoints = self.builder.spawnPoints

        # HUD
        self.hud = Hud()

    def start(self):
        self.loadLevel("assets/level")
        self.loadLights()

        # player
        self.loadPlayer("default")
        self.loadDude()

        # Timer
        taskMgr.add(self.update, "Game_Update_Task", 0)

        self.hud.show()

    def stop(self):
        #self.player.stop()
        #self.dude.stop()
        #self.physics_world = None
        render.clearLight(self.directLight)
        self.directLight = None
        self.hud.hide()

    def update(self, task):

        if self.game_counter_node == None:
            return

        ghost = self.game_counter_node.node()
        for node in ghost.getOverlappingNodes():

            if "red" in node.name:
                self.redDudesCount += 1
                self.blueDudesCount -= 1
                if self.blueDudesCount <= 0:
                    self.isLosing = True

                self.physics_world.removeRigidBody(self.dude.dudes[node.name].node())
                self.dude.dudes[node.name].removeNode()
                self.hud.update(self.redDudesCount, self.blueDudesCount)
                break


            elif "blue" in node.name:
                self.blueDudesCount += 1
                self.physics_world.removeRigidBody(self.dude.dudes[node.name].node())
                self.dude.dudes[node.name].removeNode()
                self.hud.update(self.redDudesCount, self.blueDudesCount)
                break

        return Task.cont

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
