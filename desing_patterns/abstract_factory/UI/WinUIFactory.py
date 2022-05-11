from UIFactory import UIFActory

# Type imports
from Button import Button
from Window import Window

# Instance imports
from WinButton import WinButton
from WinWindow import WinWindow


class WinUIFactory(UIFActory):
    def createButton(self) -> Button:
        return WinButton()

    def createWindow(self) -> Window:
        return WinWindow()
