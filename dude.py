#!/usr/bin/python

from datetime import datetime
from random import randint, choice
# Panda Engine imports
from panda3d.bullet import BulletSphereShape, BulletRigidBodyNode
from panda3d.core import Vec3, BitMask32, Point3, CardMaker, NodePath
from direct.task.Task import Task

# Game imports

#----------------------------------------------------------------------#

class Dude():

    def __init__(self, _parent=None):
        self.parent = _parent

        self.dudes = {}
        self.dudesToSpawn = 10

        # Spawner
        self.secondsTime = 0
        self.count = 0

    def start(self):
        taskMgr.add(self.timer, "Dude_Spawn_Timer", 0)
        taskMgr.add(self.update, "Dude_Spawner_Task", 0)

        # Start
        for x in range(0, 5):
            self.dudeSpawn()

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
        _pos = choice(self.parent.spawnPoints)#Point3(randint(-5, 5), 0, 8)

        self.count += 1

        if _type == "blue":
            # make blue dudes they are good
            body = self.createBody(self.count, _type, _pos)

        if _type == "red":
            body = self.createBodyBad(self.count, _type, _pos)

        self.dudes[body[0]] = body[1]
        #print (self.dudes)


    def createBody(self, _count, _type, _pos=(0, 0, 0)):
        radius = 0.4
        shape = BulletSphereShape(radius)

        name = _type+"Dude"+str(_count)

        node = BulletRigidBodyNode(name)
        node.setMass(2.0)
        node.addShape(shape)
        #node.setDeactivationEnabled(False)
        np = render.attachNewNode(node)
        np.setCollideMask(BitMask32.allOn())

        self.parent.physics_world.attachRigidBody(node)

        np.setPos(_pos)

        #model = loader.loadModel("assets/dude")
        #model.reparentTo(np)
        #model.setScale(0.4)

        tex = loader.loadTexture("assets/dudes/dude1_good.png")   
        cm = CardMaker('spritesMaker')
        sprite = NodePath(cm.generate())   
        sprite.setTexture(tex)
        sprite.reparentTo(np)
        sprite.setPos(-0.5, 0, -0.5)
        sprite.setCompass(render)
        sprite.setTransparency(1)

        return name, np

    def createBodyBad(self, _count, _type, _pos=(0, 0, 0)):
        radius = 0.4
        shape = BulletSphereShape(radius)

        name = _type+"Dude"+str(_count)

        node = BulletRigidBodyNode(name)
        node.setMass(2.0)
        node.addShape(shape)
        #node.setDeactivationEnabled(False)
        np = render.attachNewNode(node)
        np.setCollideMask(BitMask32.allOn())

        self.parent.physics_world.attachRigidBody(node)

        np.setPos(_pos)

        #model = loader.loadModel("assets/badDude")
        #model.reparentTo(np)
        #model.setScale(0.4)

        tex = loader.loadTexture("assets/dudes/dude1_bad.png")   
        cm = CardMaker('spritesMaker')
        sprite = NodePath(cm.generate())   
        sprite.setTexture(tex)
        sprite.reparentTo(np)
        sprite.setPos(-0.5, 0, -0.5)
        sprite.setCompass(render)
        sprite.setTransparency(1)

        return name, np