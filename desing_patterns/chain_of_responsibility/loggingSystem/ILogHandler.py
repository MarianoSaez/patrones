class ILogHandler:
    def handleLog(self, logLevel: int, msg: str) -> None:
        raise NotImplementedError

    def setNxt(self, next) -> None:
        raise NotImplementedError