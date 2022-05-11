"""
Interfaz que declara el comportamiento de las fabricas
que crearan instancias de Window y Button.
Analogo a AbstractFactory.
"""
# Type imports
from Window import Window
from Button import Button


class UIFActory:
    def createWindow(self) -> Window:
        raise NotImplementedError

    def createButton(self) -> Button:
        raise NotImplementedError
