from Component import Component


class Leaf(Component):
    def __init__(self, value: int) -> None:
        self.value = value

    def operation(self) -> int:
        print(f"[ Leaf ]: Retornando mi valor -> {self.value}")
        return self.value