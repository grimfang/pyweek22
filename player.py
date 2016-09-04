#!/usr/bin/python

# Panda Engine imports
from panda3d.bullet import BulletBoxShape, BulletRigidBodyNode, BulletHingeConstraint
from panda3d.core import Vec3, BitMask32, Point3
from direct.task.Task import Task
from direct.showbase.InputStateGlobal import inputState

# Game imports
from utils import createSprite

#----------------------------------------------------------------------#

class Player():

    def __init__(self, _parent=None):
        self.parent = _parent


    def start(self):
    	self.createDoor("assets/door.png", "Left", Vec3(-0.13, 3, -0.28))

    	# Tasks
    	taskMgr.add(self.update, "Player_Update_Task")

    def stop(self):
    	taskMgr.remove('Player_Update_Task')

    def update(self, task):

    	return task.cont

    #### BUILDERS ####
    def createDoor(self, _filename, _side, _pos):
    	self.parent.game_doors[_side] = Door(self.parent, _filename, _side, _pos)




#### DOOR CLASS ####
class Door():
	def __init__(self, _parent, _filename, _side, _pos):

		sprite = createSprite(_filename, _pos.x, _pos.z)

		shape = BulletBoxShape(Vec3(sprite[1][0]/2, 0.05, sprite[1][1]/2))
		node = BulletRigidBodyNode("Player_Door_" + _side)
		node.addShape(shape)

		self.np = _parent.game_doors_np.attachNewNode(node)
		self.np.setCollideMask(BitMask32.allOn())
		self.np.setPos(_pos)

		_parent.physics_world.attachRigidBody(node)

		# Set sprite
		#sprite[0].clearModelNodes()
		sprite[0].reparentTo(self.np)
		sprite[0].setPos(-0.02, 0, -0.145)
		#sprite[0].setPos(_pos)

		# Hinge
		pivotA = Point3(2, 0, 0)
		pivotB = Point3(-4, 0, 0)
		axisA = Vec3(0, 1, 0)
		axisB = Vec3(0, 0, 1)

		hinge = BulletHingeConstraint(node, _pos, axisA, True)
		hinge.setDebugDrawSize(2.0)
		hinge.setLimit(-90, 120, softness=0.9, bias=0.3, relaxation=1.0)
		_parent.physics_world.attachConstraint(hinge)