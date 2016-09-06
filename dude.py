#!/usr/bin/python

from datetime import datetime
from random import randint, choice
# Panda Engine imports
from panda3d.bullet import BulletSphereShape, BulletRigidBodyNode
from panda3d.core import Vec3, BitMask32, Point3
from direct.task.Task import Task

# Game imports

#----------------------------------------------------------------------#

class Dude():

    def __init__(self, _parent=None):
        self.parent = _parent

        self.dudes = []
        self.dudesToSpawn = 10

        # Spawner
        self.secondsTime = 0
        self.count = 0

    def start(self):
        taskMgr.add(self.timer, "Dude_Spawn_Timer", 0)
        taskMgr.add(self.update, "Dude_Spawner_Task", 0)

        # Start
        for x in range(-5, 5):
            if x == 0:
                pass
            else:
                self.body = self.createBody(self.count, (x, 0, 5))
                self.dudes.append(self.body)

        self.badBody = self.createBodyBad(self.count, (-2, 0, 5.5))

    def stop(self):
        for body in self.bodies:
            body.removeNode()

        self.bodies = []

    def update(self, task):
        if task.time > 3.0:
            self.dudeSpawn()
            return Task.again

        return Task.cont

    def timer(self, task):
        self.secondsTime = int(task.time)
        return Task.cont

    def dudeSpawn(self):
        choices = ["blue", "red"]

        _type = choice(choices)
        _pos = Point3(randint(-5, 5), 0, 5)

        self.count += 1

        if _type == "blue":
            # make blue dudes they are good
            body = self.createBody(self.count, _pos)

        if _type == "red":
            body = self.createBodyBad(self.count, _pos)

        self.dudes.append(body)
        print (self.dudes)


    def createBody(self, _count, _pos=(0, 0, 0)):
        radius = 0.4
        shape = BulletSphereShape(radius)

        node = BulletRigidBodyNode("Dude"+str(_count))
        node.setMass(2.0)
        node.addShape(shape)
        #node.setDeactivationEnabled(False)
        np = render.attachNewNode(node)
        np.setCollideMask(BitMask32.allOn())

        self.parent.physics_world.attachRigidBody(node)

        np.setPos(_pos)

        model = loader.loadModel("assets/dude")
        model.reparentTo(np)
        model.setScale(0.4)

        return np

    def createBodyBad(self, _count, _pos=(0, 0, 0)):
        radius = 0.4
        shape = BulletSphereShape(radius)

        node = BulletRigidBodyNode("Dude"+str(_count))
        node.setMass(2.0)
        node.addShape(shape)
        #node.setDeactivationEnabled(False)
        np = render.attachNewNode(node)
        np.setCollideMask(BitMask32.allOn())

        self.parent.physics_world.attachRigidBody(node)

        np.setPos(_pos)

        model = loader.loadModel("assets/badDude")
        model.reparentTo(np)
        model.setScale(0.4)

        return np