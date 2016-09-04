#!/usr/bin/python

import sys

# Panda Engine imports
from panda3d.core import loadPrcFileData
loadPrcFileData("",
"""
    window-title PyWeek22
    fullscreen 0
    win-size 1260 876
    cursor-hidden 0
    sync-video 1
    show-frame-rate-meter 1

"""
)

from direct.showbase.ShowBase import ShowBase

# Game imports
from gamebase import GameBase

#----------------------------------------------------------------------#

class Main(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
        # Set esc for force exit
        self.accept('escape', self.exitApp)

        ## Load/Start GameBase
        self.gamebase = GameBase()
        self.gamebase.start()

        # Debug #
        self.gamebase.enablePhysicsDebug()
        print (render.ls())


    def exitApp(self):
        sys.exit()
        
main = Main()
main.run()