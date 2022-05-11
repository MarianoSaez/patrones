from calendar import IllegalMonthError
from ILogHandler import ILogHandler


class ErrorLogger(ILogHandler):
    def __init__(self, nxt: ILogHandler = None) -> None:
        super().__init__()
        self.nxt = nxt

    def setNxt(self, next) -> None:
        self.nxt = next

    def handleLog(self, logLevel: int, msg: str) -> None:
        if 1 <= logLevel < 2:
            print(f"[ ERROR ]: {msg}")
        else:
            if self.nxt is not None:
                self.nxt.handleLog(logLevel, msg)
