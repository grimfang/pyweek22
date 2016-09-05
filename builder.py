#!/usr/bin/python

# Panda Engine imports
from panda3d.bullet import BulletBoxShape, BulletRigidBodyNode, BulletHingeConstraint, BulletPlaneShape
from panda3d.core import Vec3, BitMask32, Point3

# Game imports

#----------------------------------------------------------------------#

class Builder():

    def __init__(self, _parent=None):
        self.parent = _parent

        self.objectTypes = {"background": self.setupBackground,
        	"door_hinge": self.setupDoorHinge,
        	"door": self.setupDoor}

        self.hinges = {}

    def parseEggFile(self, _filename):

    	eggFile = loader.loadModel(_filename)

    	# Get the contained objects
    	objects = eggFile.findAllMatches('**')

    	for obj in objects:
    		for types in self.objectTypes:
    			if obj.hasTag(types):
    				self.objectTypes[types](obj, eggFile)


    def setupBackground(self, _obj, _eggFile):
    	shape = BulletPlaneShape(Vec3(0, 0.1, 0), 1)
    	node = BulletRigidBodyNode(_obj.getTag("background"))
    	node.addShape(shape)
    	np = render.attachNewNode(node)
    	np.setCollideMask(BitMask32.allOn())
    	self.parent.physics_world.attachRigidBody(node)

    	_obj.reparentTo(render)
    	_obj.setPos(0, 0, 0)

    def setupDoorHinge(self, _obj, _eggFile):
    	self.hinges[_obj.getTag("door_hinge")] = Point3(_obj.getPos())
    	# example: self.hinges["left"] = Pos

    def setupDoor(self, _obj, _eggFile):
    	pass