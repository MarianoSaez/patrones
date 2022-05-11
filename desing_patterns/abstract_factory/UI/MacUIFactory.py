from UIFactory import UIFActory

# Type imports
from Button import Button
from Window import Window

# Instance imports
from MacButton import MacButton
from MacWindow import MacWindow


class MacUIFactory(UIFActory):
    def createWindow(self) -> Window:
        return MacWindow()

    def createButton(self) -> Button:
        return MacButton()