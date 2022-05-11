from ILogHandler import ILogHandler


class ConsoleLogger(ILogHandler):
    def __init__(self, nxt: ILogHandler = None) -> None:
        super().__init__()
        self.nxt = nxt

    def setNxt(self, next) -> None:
        self.nxt = next

    def handleLog(self, logLevel: int, msg: str) -> None:
        if logLevel < 1:
            print(f"[ INFO ]: {msg}")
        else:
            if self.nxt is not None:
                self.nxt.handleLog(logLevel, msg)
