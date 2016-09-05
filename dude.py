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

        self.bodies = []

    def start(self):
        for x in range(-5, 5):
            if x == 0:
                pass
            else:
                self.body = self.createBody((x, 0, 5))
                self.bodies.append(self.body)

        self.badBody = self.createBodyBad((-2, 0, 5.5))

    def stop(self):
        for body in self.bodies:
            body.removeNode()

        self.bodies = []


    def createBody(self, _pos=(0, 0, 0)):
        radius = 0.4
        shape = BulletSphereShape(radius)

        node = BulletRigidBodyNode("Dude")
        node.setMass(2.0)
        node.addShape(shape)
        node.setDeactivationEnabled(False)
        np = render.attachNewNode(node)
        np.setCollideMask(BitMask32.allOn())

        self.parent.physics_world.attachRigidBody(node)

        np.setPos(_pos)

        model = loader.loadModel("assets/dude")
        model.reparentTo(np)
        model.setScale(0.4)

        return np

    def createBodyBad(self, _pos=(0, 0, 0)):
        radius = 0.4
        shape = BulletSphereShape(radius)

        node = BulletRigidBodyNode("Dude")
        node.setMass(2.0)
        node.addShape(shape)
        node.setDeactivationEnabled(False)
        np = render.attachNewNode(node)
        np.setCollideMask(BitMask32.allOn())

        self.parent.physics_world.attachRigidBody(node)

        np.setPos(_pos)

        model = loader.loadModel("assets/badDude")
        model.reparentTo(np)
        model.setScale(0.4)

        return np