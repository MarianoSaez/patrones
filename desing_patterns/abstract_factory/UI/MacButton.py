from Button import Button


class MacButton(Button):
    def onClick(self) -> None:
        print(f"[ {type(self)} ]: Me presionaste!")
