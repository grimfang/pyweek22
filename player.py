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
    	base.ignore("arrow_left")
    	base.ignore("arrow_right")
    	base.ignore("z")
    	base.ignore("/")
    	taskMgr.remove('Player_Update_Task')
    	self.parent.game_doors = {}

    def update(self, task):
    	if inputState.isSet('left'):
    		#self.parent.game_doors['left'].node().applyTorque(Vec3(0, -150, 0))
    		pass

    	else:
    		self.parent.game_doors['left'].node().applyTorque(Vec3(0, 150, 0))
    		self.parent.game_doors['left_hinge'].enableMotor(False)

    	if inputState.isSet('right'):
    		#self.parent.game_doors['right'].node().applyTorque(Vec3(0, 150, 0))
    		pass

    	else:
    		self.parent.game_doors['right'].node().applyTorque(Vec3(0, -150, 0))
    		self.parent.game_doors['right_hinge'].enableMotor(False)
    		#print (getMousePos())
    	return task.cont

    def leftAction(self):
    	#self.parent.game_doors['left'].node().applyTorqueImpulse(Vec3(0, -100, 0))
    	self.parent.game_doors['left_hinge'].enableAngularMotor(True, 20.0, 15.0)

    def rightAction(self):
    	#self.parent.game_doors['right'].node().applyTorqueImpulse(Vec3(0, 100, 0))
    	#ulimit = self.parent.game_doors['right_hinge'].getUpperLimit()
    	self.parent.game_doors['right_hinge'].enableAngularMotor(True, 20.0, 15.0)