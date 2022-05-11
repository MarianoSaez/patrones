# Type imports
from UIFactory import UIFActory
from Button import Button
from Window import Window

# Conf imports
from conf import factory


class Application:
    def __init__(self, factory: UIFActory) -> None:
        self.factory: UIFActory = factory
        self.window: Window = None
        self.button: Button = None

    def run(self) -> None:
        self.window = self.factory.createWindow()
        self.button = self.factory.createButton()

if __name__ == "__main__":
    """
    Vemos como la app no esta al tanto de cual de las fabricas esta utilizando,
    todo fue definido en el archivo de configuracion, y solo es necesario que sepa
    que la fabrica que posee cumple con la interfaz UIFactory, y que por la tanto
    es capaz de crear boton y ventanas, cuyas clases concretas tampoco conoce.
    """
    app = Application(factory)
    app.run()

    # Simular uso
    app.window.openWindow()
    app.button.onClick()
    app.window.closeWindow()
