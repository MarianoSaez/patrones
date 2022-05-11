from Button import Button


class WinButton(Button):
    def onClick(self) -> None:
        print(f"[ {type(self)} ]: Me presionaste!")
