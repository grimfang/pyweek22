#!/usr/bin/python

# Panda Engine imports
from panda3d.bullet import BulletWorld, BulletDebugNode
from panda3d.core import Vec3, OrthographicLens
from direct.task.Task import Task

# Game imports

#----------------------------------------------------------------------#

class GameBase():

    def __init__(self, _parent=None):
        self.parent = _parent

        # Physics
        self.gravity = Vec3(0, 0, 0)
        self.physics_world = None

        # Camera
        self.cam_position = Vec3(0, 0, 0)
        self.cam_rotation = (-90.0, 0.0, 0.0)

    def start(self):
    	# Physics
    	self.setupPhysics(self.gravity)

    	# Camera
    	self.setupCamera(self.cam_position, self.cam_rotation)

    	# Start Tasks
    	taskMgr.add(self.updatePhysics, 'update-physics-task', 0)

    def stop(self):
    	# Stop Tasks
    	taskMgr.remove("update-physics-task")

    	# reset objects
    	self.physics_world = None

    ##### SETUPS #####
    def setupPhysics(self, _gravity):
    	self.physics_world = BulletWorld()
    	self.physics_world.setGravity(_gravity)


    def setupCamera(self, _pos, _rot):
    	lens = OrthographicLens()
    	lens.setFilmSize(20, 15)
    	base.cam.node().setLens(lens)
    	base.cam.setPos(_pos)
    	base.cam.setHpr(_rot)

    ##### UPDATES #####
    def updatePhysics(self, task):
    	dt = globalClock.getDt()
    	self.physics_world.doPhysics(dt, 5, 1.0/240.0)

    	return task.cont

    ##### DEBUG #####
    def enablePhysicsDebug(self):
    	debugnode = BulletDebugNode('Physics-Debug')
    	debugnode.showWireframe(True)
    	debugnode.showConstraints(True)

    	debugNP = render.attachNewNode(debugnode)
    	if self.physics_world != None:
    		self.physics_world.setDebugNode(debugNP.node())