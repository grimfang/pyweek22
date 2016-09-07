#!/usr/bin/python

# Python imports
import random
import sys

# Panda Engine imports
from panda3d.core import (
    loadPrcFileData,
    loadPrcFile,
    AntialiasAttrib,
    TextNode,
    CardMaker,
    NodePath,
    TransparencyAttrib,
    TextureStage,
    LVecBase4f,)
from direct.interval.IntervalGlobal import Sequence
from direct.interval.FunctionInterval import (
    Wait,
    Func)
from direct.interval.LerpInterval import LerpColorScaleInterval
loadPrcFileData("",
"""
    window-title Grimfang - PyWeek22 - bouncer
    cursor-hidden 0
    model-path $MAIN_DIR/assets/
"""
)
loadPrcFile("./mainConfig.prc")
from direct.showbase.ShowBase import ShowBase
from direct.fsm.FSM import FSM
from direct.gui.DirectGui import DGG
from pandac.PandaModules import WindowProperties

# Game imports
from gamebase import GameBase
from game import Game
from mainmenu import MainMenu
from optionsmenu import OptionsMenu
from direct.gui.DirectGui import DirectLabel


def hide_cursor():
    """set the Cursor invisible"""
    props = WindowProperties()
    props.setCursorHidden(True)
    # somehow the window gets undecorated after hiding the cursor
    # so we reset it here to the value we need
    # props.setUndecorated(settings.fullscreen)
    base.win.requestProperties(props)


def show_cursor():
    """set the Cursor visible again"""
    props = WindowProperties()
    props.setCursorHidden(False)
    # set the filename to the mouse cursor
    cursors = ["cursorRed", "cursorBlue", "cursorViolet", "cursorGreen"]
    cursor = random.choice(cursors)
    x11 = "cursors/{}.x11".format(cursor)
    win = "assets/{}.ico".format(cursor)
    if sys.platform.startswith("linux"):
        props.setCursorFilename(x11)
    else:
        props.setCursorFilename(win)
    base.win.requestProperties(props)
#----------------------------------------------------------------------#

class Main(ShowBase, FSM):

    def __init__(self):
        ShowBase.__init__(self)
        FSM.__init__(self, "mainStateMachine")

        # some basic enhancements
        # window background color
        self.setBackgroundColor(0, 0, 0)
        # set antialias for the complete sceen to automatic
        self.render.setAntialias(AntialiasAttrib.MAuto)
        # shader generator
        render.setShaderAuto()
        # Enhance font readability
        DGG.getDefaultFont().setPixelsPerUnit(100)
        # hide the mouse cursor
        hide_cursor()

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

        ## Load music list
        self.musicList = [
            ["Housewell - Housewell - Sea  Sun  Fun", loader.loadMusic("music/Housewell_-_Housewell_-_Sea__Sun__Fun.ogg")],
            ["KontrastE - LISTEN TO NIGHT", loader.loadMusic("music/KontrastE_-_LISTEN_TO_NIGHT.ogg")],
            ["LukHash - THE OTHER SIDE", loader.loadMusic("music/LukHash_-_THE_OTHER_SIDE.ogg")],]
        self.lblNowPlaying = DirectLabel(
            text="No track running!",
            text_align=TextNode.ARight,
            text_fg=(240/255.0,255/255.0,240/255.0,0.75),
            pos=(base.a2dRight-0.05, 0, base.a2dBottom+0.05),
            scale=0.04,
            frameColor=(0,0,0,0.5),)
        self.lblNowPlaying.hide()

        # The games Intro
        def create16To9LogoCard(logoPath, tsName):
            cm = CardMaker("fade")
            scale = abs(base.a2dLeft) / 1.7776
            cm.setFrame(-1, 1, -1*scale, 1*scale)
            logo = NodePath(cm.generate())
            logo.setTransparency(TransparencyAttrib.MAlpha)
            logoTex = loader.loadTexture(logoPath)
            logoTs = TextureStage(tsName)
            logoTs.setMode(TextureStage.MReplace)
            logo.setTexture(logoTs, logoTex)
            logo.setBin("fixed", 5000)
            logo.reparentTo(render2d)
            logo.hide()
            return logo
        self.gfLogo = create16To9LogoCard("intro/GrimFangLogo.png", "gfLogoTS")
        self.pandaLogo = create16To9LogoCard("intro/Panda3DLogo.png", "pandaLogoTS")
        self.gameLogo = create16To9LogoCard("intro/GameLogo.png", "gameLogoTS")
        def createFadeIn(logo):
            return LerpColorScaleInterval(
                logo,
                2,
                LVecBase4f(0.0, 0.0, 0.0, 1.0),
                LVecBase4f(0.0, 0.0, 0.0, 0.0))
        def createFadeOut(logo):
            return LerpColorScaleInterval(
                logo,
                2,
                LVecBase4f(0.0, 0.0, 0.0, 0.0),
                LVecBase4f(0.0, 0.0, 0.0, 1.0))
        gfFadeInInterval = createFadeIn(self.gfLogo)
        gfFadeOutInterval = createFadeOut(self.gfLogo)
        p3dFadeInInterval = createFadeIn(self.pandaLogo)
        p3dFadeOutInterval = createFadeOut(self.pandaLogo)
        gameFadeInInterval = createFadeIn(self.gameLogo)
        gameFadeOutInterval = createFadeOut(self.gameLogo)
        self.introFadeInOutSequence = Sequence(
            Func(self.gfLogo.show),
            gfFadeInInterval,
            Wait(1.0),
            gfFadeOutInterval,
            Wait(0.5),
            Func(self.gfLogo.hide),
            Func(self.pandaLogo.show),
            p3dFadeInInterval,
            Wait(1.0),
            p3dFadeOutInterval,
            Wait(0.5),
            Func(self.pandaLogo.hide),
            Func(self.gameLogo.show),
            gameFadeInInterval,
            Wait(1.0),
            gameFadeOutInterval,
            Wait(0.5),
            Func(self.gameLogo.hide),
            Func(self.messenger.send, "intro_done"),
            Func(self.startMusic),
            name="fadeInOut")
        # game intro end

        #
        # Start with the menu after the intro has been played
        #
        self.introFadeInOutSequence.start()
        self.accept("intro_done", self.request, ["Menu"])


    def exitApp(self):
        if self.state == "Off":
            self.introFadeInOutSequence.finish()
        elif self.state == "Menu":
            self.userExit()
        else:
            self.request("Menu")

    def startMusic(self):
        self.lblNowPlaying.show()
        self.lastPlayed = None
        self.currentTrack = [None]
        self.playNextTrack()
        base.taskMgr.add(self.musicTask, "music playlist")

    def playNextTrack(self):
        while self.lastPlayed == self.currentTrack[0]:
            self.currentTrack = random.choice(self.musicList)
        self.lastPlayed = self.currentTrack[0]
        self.lblNowPlaying["text"] = "NOW PLAYING: {}".format(self.currentTrack[0])
        self.currentTrack[1].play()

    def musicTask(self, task):
        if not base.AppHasAudioFocus: return task.cont
        track = self.currentTrack[1]
        if track.status() != track.PLAYING:
            self.playNextTrack()
        return task.cont

    def enterMenu(self):
        show_cursor()
        self.mainMenu.show()

    def exitMenu(self):
        self.mainMenu.hide()

    def enterOptions(self):
        self.optionsMenu.show()

    def exitOptions(self):
        self.optionsMenu.hide()

    def enterGame(self):
        hide_cursor()
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
