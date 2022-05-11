from IHandler import IHandler


class ConcreteHandler3(IHandler):
    def __init__(self, nxt: IHandler = None) -> None:
        super().__init__()
        self.nxt = nxt

    def handle(self, request: int) -> None:
        if 20 <= request:
            print(f"[ {type(self)} ] Puedo manejarlo! Valor: {request}")
        else:
            if self.nxt is not None:
                self.nxt.handle(request)

    def setNext(self, nxt) -> None:
        self.nxt = nxt