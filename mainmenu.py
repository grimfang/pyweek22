from direct.gui.DirectGui import (
    DirectFrame,
    DirectButton,
    OnscreenImage,)

class MainMenu():
    def __init__(self):
        self.frameMain = DirectFrame(
            image="mainmenu.png",
            image_scale=(1.7778, 1, 1),
            frameSize=(
                base.a2dLeft, base.a2dRight,
                base.a2dBottom, base.a2dTop),
            frameColor=(0, 0, 0, 0))
        self.frameMain.setTransparency(True)

        self.btnStart = DirectButton(
            text="Enter",
            scale=0.15,
            text_pos=(0, 1.1),
            text_scale=0.5,
            text_fg=(240/255.0,255/255.0,240/255.0,1),
            frameColor=(0, 0, 0, 0),
            image=("btnEnter.png", "btnEnter_hover.png", "btnEnter_hover.png", "btnEnter_hover.png"),
            pos=(0, 0, -0.5),
            command=base.messenger.send,
            extraArgs=["menu_StartGame"])
        self.btnStart.setTransparency(True)
        self.btnStart.reparentTo(self.frameMain)

        self.btnOptions = DirectButton(
            text="Options",
            scale=0.1,
            pos=(base.a2dRight-0.2, 0, base.a2dBottom+0.2),
            command=base.messenger.send,
            extraArgs=["menu_Options"])
        self.btnOptions.setTransparency(True)
        self.btnOptions.reparentTo(self.frameMain)

        self.btnQuit = DirectButton(
            text="Exit",
            scale=0.15,
            text_pos=(-0.3, -0.25),
            text_scale=0.75,
            text_fg=(240/255.0,255/255.0,240/255.0,1),
            frameColor=(0, 0, 0, 0),
            image=("btnExit.png", "btnExit_hover.png", "btnExit_hover.png", "btnExit_hover.png"),
            image_scale=(1, 1, 0.5),
            pos=(base.a2dLeft+0.3, 0, base.a2dBottom+0.25),
            command=base.messenger.send,
            extraArgs=["menu_QuitGame"])
        self.btnQuit.setTransparency(True)
        self.btnQuit.reparentTo(self.frameMain)


        self.imgBouncer = OnscreenImage(
            image="bouncer.png",
            scale=(0.75*0.25, 1*0.25, 1*0.25),
            pos=(-0.25, 0, -0.5))
        self.imgBouncer.setTransparency(True)
        self.imgBouncer.reparentTo(self.frameMain)


        self.hide()

    def show(self):
        self.frameMain.show()

    def hide(self):
        self.frameMain.hide()
