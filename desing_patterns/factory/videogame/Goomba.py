"""
Subclase que implementa la interfaz Entity. Analogo
a ConcreteProduct.
"""


from Entity import Entity


class Goomba(Entity):
    def __init__(self, level: int, x: float, y: float) -> None:
        self.level = level
        self.x = x
        self.y = y

        print(f"[ Goomba ]: LVL: {self.level} ha aparecido en ( {self.x}, {self.y} )")

    def move(self, x: float, y: float) -> None:
        print(f"Cambiando coordenadas a ( {x}, {y} )")
        self.x = x
        self.y = y