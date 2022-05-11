from Writer import Writer


class ScreenWriter(Writer):
    def write(self, string: str) -> None:
        print(string)
