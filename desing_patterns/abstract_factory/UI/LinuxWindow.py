from Window import Window


class LinuxWindow(Window):
    def openWindow(self) -> None:
        print(f"[ {type(self)} ]: Abriendo ventana!")

    def closeWindow(self) -> None:
        print(f"[ {type(self)} ]: Cerrando ventana!")
