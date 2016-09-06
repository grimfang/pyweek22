#!/usr/bin/python

# Panda Engine imports
from panda3d.core import (
    loadPrcFileData,
    AntialiasAttrib,)
loadPrcFileData("",
"""
    window-title PyWeek22
    fullscreen 0
    #win-size 1260 876
    cursor-hidden 0
    sync-video 1
    show-frame-rate-meter 1
    textures-auto-power-2 1
    model-path $MAIN_DIR/assets/
    framebuffer-multisample 1
    multisamples 8
    texture-anisotropic-degree 0
"""
)
from direct.showbase.ShowBase import ShowBase
from direct.fsm.FSM import FSM
from direct.gui.DirectGui import DGG

# Game imports
from gamebase import GameBase
from game import Game
from mainmenu import MainMenu
from optionsmenu import OptionsMenu

#----------------------------------------------------------------------#

class Main(ShowBase, FSM):

    def __init__(self):
        ShowBase.__init__(self)
        FSM.__init__(self, "mainStateMachine")

        # some basic enhancements
        # set antialias for the complete sceen to automatic
        self.render.setAntialias(AntialiasAttrib.MAuto)
        # shader generator
        render.setShaderAuto()
        # Enhance font readability
        DGG.getDefaultFont().setPixelsPerUnit(100)

        # Set esc to force exit $ remove
        self.accept('escape', self.exitApp)

        # Menu Events
        self.accept("menu_StartGame", self.request, ["Game"])
        self.accept("menu_Options", self.request, ["Options"])
        self.accept("menu_QuitGame", self.exitApp)
        self.accept("menu_Back", self.request, ["Menu"])

        ## Load Menu
        self.mainMenu = MainMenu()
        self.optionsMenu = OptionsMenu()

        ## Load/Start GameBase
        self.gamebase = GameBase()

        ## Load/Start Game
        self.game = Game()

        self.request("Menu")


    def exitApp(self):
        if self.state == "Menu":
            self.userExit()
        else:
            self.request("Menu")

    def enterMenu(self):
        self.mainMenu.show()

    def exitMenu(self):
        self.mainMenu.hide()

    def enterOptions(self):
        self.optionsMenu.show()

    def exitOptions(self):
        self.optionsMenu.hide()

    def enterGame(self):
        self.gamebase.start()
        self.game.setPhysicsWorld(self.gamebase.physics_world)
        self.game.start()

        # Debug #
        #self.gamebase.enablePhysicsDebug()
        #print (render.ls())

    def exitGame(self):
        self.game.stop()
        self.gamebase.stop()

main = Main()
main.run()
