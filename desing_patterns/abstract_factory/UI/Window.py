"""
Interfaz que declara comportamiento de una ventana grafica.
Analogo a alguna clase Product.
"""
class Window:
    def openWindow(self) -> None:
        raise NotImplementedError

    def closeWindow(self) -> None:
        raise NotImplementedError
