from Reader import Reader


class KeyboardReader(Reader):
    def read(self) -> str:
        return input()