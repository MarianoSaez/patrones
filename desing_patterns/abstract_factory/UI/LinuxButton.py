from Button import Button


class LinuxButton(Button):
    def onClick(self) -> None:
        print(f"[ {type(self)} ]: Me presionaste!")
