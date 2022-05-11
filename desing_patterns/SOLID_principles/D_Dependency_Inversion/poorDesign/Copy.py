from ReadKeyboard import ReadKeyboard
from WriteScreen import WriteScreen


class Copy:
    def __init__(self) -> None:
        self.keyboard = ReadKeyboard()  # Dependencia
        self.screen = WriteScreen()     # Dependencia

    def copy(self) -> None:
        while (c := self.keyboard.read()) != "^":
            self.screen.write(c)
