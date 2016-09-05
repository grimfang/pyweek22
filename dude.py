#!/usr/bin/python

# Panda Engine imports
from panda3d.bullet import BulletSphereShape, BulletRigidBodyNode
from panda3d.core import Vec3, BitMask32, Point3
from direct.task.Task import Task

# Game imports

#----------------------------------------------------------------------#

class Dude():

    def __init__(self, _parent=None):
        self.parent = _parent

        self.body = None


    def start(self):
        # Tasks
        taskMgr.add(self.update, "Dude_Update_Task")
        self.createBody()

    def stop(self):
    	taskMgr.remove('Dude_Update_Task')

    def update(self, task):
    	return task.cont

    def createBody(self):
        radius = 0.4
        shape = BulletSphereShape(radius)

        node = BulletRigidBodyNode("Dude")
        node.setMass(5)
        node.addShape(shape)
        node.setDeactivationEnabled(False)
        np = render.attachNewNode(node)
        np.setCollideMask(BitMask32.allOn())

        self.parent.physics_world.attachRigidBody(node)

        self.body = np