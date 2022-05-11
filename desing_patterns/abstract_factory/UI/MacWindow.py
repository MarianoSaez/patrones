from Window import Window


class MacWindow(Window):
    def openWindow(self) -> None:
        print(f"[ {type(self)} ]: Abriendo ventana!")

    def closeWindow(self) -> None:
        print(f"[ {type(self)} ]: Cerrando ventana!")
