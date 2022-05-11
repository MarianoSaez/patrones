class IHandler:
    def handle(self, request: int) -> None:
        raise NotImplementedError

    def setNext(self, nxt) -> None:
        raise NotImplementedError