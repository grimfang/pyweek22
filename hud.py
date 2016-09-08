from panda3d.core import Point3, TextNode
from direct.gui.DirectGui import (
    DirectFrame,
    DirectLabel,)

class Hud():
    def __init__(self):
        self.frameMain = DirectFrame(
            image="hudBackground.png",
            image_scale=(0.4444445, 1, 1),
            frameSize=(
                base.a2dLeft/4.0, base.a2dRight/4.0,
                base.a2dBottom, base.a2dTop),
            frameColor=(0, 0, 0, 0),
            pos=(base.a2dLeft/1.33333, 0, 0))
        self.frameMain.setTransparency(True)

        self.frameRightPane = DirectFrame(
            image="hudBackgroundRight.png",
            image_scale=(0.4444445, 1, 1),
            frameSize=(
                base.a2dRight/4.0, base.a2dLeft/4.0,
                base.a2dBottom, base.a2dTop),
            frameColor=(0, 0, 0, 0),
            pos=(base.a2dRight/1.33333, 0, 0))
        self.frameRightPane.setTransparency(True)
        self.hide()

        self.lblScore = DirectLabel(
            text="Scoreboard",
            text_fg=(240/255.0,255/255.0,240/255.0,1),
            scale=0.1,
            pos=(0,0,0.8),
            frameColor=(0,0,0,0),)
        self.lblScore.setTransparency(True)
        self.lblScore.reparentTo(self.frameMain)

        self.lblReds = DirectLabel(
            text="Bad dudes: 0",
            text_fg=(240/255.0,255/255.0,240/255.0,1),
            text_align=TextNode.ALeft,
            scale=0.1,
            pos=(-0.4,0,0.5),
            frameColor=(0,0,0,0),)
        self.lblReds.setTransparency(True)
        self.lblReds.reparentTo(self.frameMain)

        self.lblBlues = DirectLabel(
            text="Good dudes: 0",
            text_fg=(240/255.0,255/255.0,240/255.0,1),
            text_align=TextNode.ALeft,
            scale=0.1,
            pos=(-0.4,0,0.3),
            frameColor=(0,0,0,0),)
        self.lblReds.setTransparency(True)
        self.lblBlues.reparentTo(self.frameMain)
        self.hide()

    def show(self):
        self.frameMain.show()
        self.frameRightPane.show()

    def hide(self):
        self.frameMain.hide()
        self.frameRightPane.hide()

    def update(self, redDudes, blueDudes):
        self.lblReds["text"] = "Bad dudes: {}".format(redDudes)
        self.lblBlues["text"] = "Good dudes: {}".format(blueDudes)
