#!/usr/bin/python

# Panda Engine imports
from panda3d.core import CardMaker, NodePath

# Game imports
from utils import createSprite

#----------------------------------------------------------------------#

class Game():

    def __init__(self, _parent=None):
        self.parent = _parent


    def start(self):
    	self.loadLevel("assets/idea.png", 0)

    def stop(self):
    	pass


    def loadLevel(self, _filename, z):
    	tex = loader.loadTexture(_filename)   
    	cm = CardMaker('Background')
    	sprite = NodePath(cm.generate())   
    	sprite.setTexture(tex)
    	sprite.setPos(-0.5, z, -0.5)

    	sprite.reparentTo(render)

