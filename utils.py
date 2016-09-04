#!/usr/bin/python

# Panda Engine imports
from panda3d.core import CardMaker, NodePath

#----------------------------------------------------------------------#

def createSprite(filename, x, z, transparent=1):   
    tex = loader.loadTexture(filename)   
    cm = CardMaker('spritesMaker')
    sprite = NodePath(cm.generate())   
    sprite.setTexture(tex)
   
    #Scale and position
    sx = float(tex.getXSize()) / base.win.getXSize()
    sz = float(tex.getYSize()) / base.win.getYSize()
    sprite.setScale(sx, 1.0, sz)
    sprite.setPos(x, 0.0, z)
    sprite.setTransparency(transparent)
    return sprite