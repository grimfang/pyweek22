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
        	"door": self.setupDoor}

        self.hingeLeft = None
        self.hingeRight = None
        self.isHingeLeftSet = False
        self.isHingeRightSet = False

    def parseEggFile(self, _filename):

    	eggFile = loader.loadModel(_filename)

    	# Get the contained objects
    	objects = eggFile.findAllMatches('**')
    	self.hingeLeft = eggFile.find("**/hinge_left")
    	self.hingeRight = eggFile.find("**/hinge_right")

    	for obj in objects:
    		for types in self.objectTypes:
    			if obj.hasTag(types):
    				self.objectTypes[types](obj, eggFile)


    def setupBackground(self, _obj, _eggFile):
    	shape = BulletPlaneShape(Vec3(0, 0.1, 0), 1)
    	node = BulletRigidBodyNode(_obj.getTag("background"))
    	node.addShape(shape)
    	np = render.attachNewNode(node)
    	#np.setCollideMask(BitMask32.allOn())
    	self.parent.physics_world.attachRigidBody(node)

    	_obj.reparentTo(render)
    	_obj.setPos(0, 0, 0)

    def setupDoorHinge(self, _obj, _eggFile):
    	pass

    def setupDoor(self, _obj, _eggFile):
    	shape = BulletBoxShape(Vec3(1.6, 0.4, 0.4))
    	node = BulletRigidBodyNode(_obj.getTag("door"))
    	node.addShape(shape)
    	node.setMass(1)
    	node.setDeactivationEnabled(False)

    	np = render.attachNewNode(node)
    	#np.setCollideMask(BitMask32.allOn())
    	np.setPos(_obj.getPos())
    	np.setHpr(_obj.getHpr())

    	self.parent.physics_world.attachRigidBody(node)

    	#_obj.reparentTo(render)

    	# Setup hinge
    	if _obj.getTag("door") == "left" and self.isHingeLeftSet != True:
    		pos = Point3(-2.5, 0, 0)#hingeLeft.getPos()
    		axisA = Vec3(0, 1, 0)
    		hinge = BulletHingeConstraint(node, pos, axisA, True)
    		hinge.setDebugDrawSize(0.3)
    		hinge.setLimit(-110, 15, softness=0.9, bias=0.3, relaxation=1.0)
    		self.parent.physics_world.attachConstraint(hinge)
    		self.isHingeLeftSet = True

    	if _obj.getTag("door") == "right" and self.isHingeRightSet != True:
    		pos = Point3(2.5, 0, 0)#hingeLeft.getPos()
    		axisA = Vec3(0, 1, 0)
    		hinge = BulletHingeConstraint(node, pos, axisA, True)
    		hinge.setDebugDrawSize(0.3)
    		hinge.setLimit(15, -110, softness=0.9, bias=0.3, relaxation=1.0)
    		self.parent.physics_world.attachConstraint(hinge)
    		self.isHingeRightSet = True

