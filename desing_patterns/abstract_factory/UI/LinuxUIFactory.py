"""
Analogo a alguna ConcreteFactory.
"""
from UIFactory import UIFActory

# Type imports
from Button import Button
from Window import Window

# Instance imports
from LinuxButton import LinuxButton
from LinuxWindow import LinuxWindow


class LinuxUIFactory(UIFActory):
    def createButton(self) -> Button:
        return LinuxButton()

    def createWindow(self) -> Window:
        return LinuxWindow()