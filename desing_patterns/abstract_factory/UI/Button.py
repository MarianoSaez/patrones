"""
Interfaz que declara el comportamiento de un boton.
Analogo a alguna interfaz Product.
"""
class Button:
    def onClick(self) -> None:
        raise NotImplementedError
