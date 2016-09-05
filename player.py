#!/usr/bin/python

# Panda Engine imports
from panda3d.bullet import BulletBoxShape, BulletRigidBodyNode, BulletHingeConstraint
from panda3d.core import Vec3, BitMask32, Point3
from direct.task.Task import Task
from direct.showbase.InputStateGlobal import inputState

# Game imports

#----------------------------------------------------------------------#

class Player():

    def __init__(self, _parent=None):
        self.parent = _parent


    def start(self):
    	# Tasks
    	taskMgr.add(self.update, "Player_Update_Task")
    	base.accept("arrow_left", self.leftAction)
    	base.accept("arrow_right", self.rightAction)
    	base.accept("z", self.leftAction)
    	base.accept("/", self.rightAction)

    def stop(self):
    	taskMgr.remove('Player_Update_Task')

    def update(self, task):
    	if inputState.isSet('left'):
    		self.parent.game_doors['left'].node().applyTorque(Vec3(0, -100, 0))

    	else:
    		self.parent.game_doors['left'].node().applyTorque(Vec3(0, 100, 0))

    	if inputState.isSet('right'):
    		self.parent.game_doors['right'].node().applyTorque(Vec3(0, 100, 0))

    	else:
    		self.parent.game_doors['right'].node().applyTorque(Vec3(0, -100, 0))
    		#print (getMousePos())
    	return task.cont

    def leftAction(self):
    	self.parent.game_doors['left'].node().applyTorqueImpulse(Vec3(0, -100, 0))

    def rightAction(self):
    	self.parent.game_doors['right'].node().applyTorqueImpulse(Vec3(0, 100, 0))
