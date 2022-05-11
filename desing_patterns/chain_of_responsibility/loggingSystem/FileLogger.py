from ILogHandler import ILogHandler


class FileLogger(ILogHandler):
    def __init__(self, nxt: ILogHandler = None) -> None:
        super().__init__()
        self.path = "path/to/file"
        self.nxt = nxt

    def setNxt(self, next) -> None:
        self.nxt = next

    def handleLog(self, logLevel: int, msg: str) -> None:
        if 2 <= logLevel < 3:
            print(f"[ FILE ]: Informacion almacenada en {self.path}")
            # Guardar mensaje en disco
        else:
            if self.nxt is not None:
                self.nxt.handleLog(logLevel, msg)