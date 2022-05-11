"""
Interfaz para entidades del juego. Analoga a IProduct.
"""
class Entity:
    def move(self, x: float, y: float) -> None:
        raise NotImplementedError
