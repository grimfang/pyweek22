from direct.gui.DirectGui import (
    DirectFrame,
    DirectButton)

class OptionsMenu():
    def __init__(self):
        self.frameMain = DirectFrame(
            image="optionsmenu.png",
            image_scale=(1.7778, 1, 1),
            frameSize=(
                base.a2dLeft, base.a2dRight,
                base.a2dBottom, base.a2dTop),
            frameColor=(0, 0, 0, 0))
        self.frameMain.setTransparency(True)

        self.btnBack = DirectButton(
            text="Back",
            scale=0.1,
            pos=(base.a2dLeft+0.2, 0, base.a2dBottom+0.2),
            command=base.messenger.send,
            extraArgs=["menu_Back"])
        self.btnBack.setTransparency(True)
        self.btnBack.reparentTo(self.frameMain)

        self.hide()

    def show(self):
        self.frameMain.show()

    def hide(self):
        self.frameMain.hide()
