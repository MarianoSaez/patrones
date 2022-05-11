from IObserver import IObserver


class ISubject():
    def addObserver(self, observer: IObserver) -> None:
        raise NotImplementedError

    def removeObserver(self, observer: IObserver) -> None:
        raise NotImplementedError

    def notify(self) -> None:
        raise NotImplementedError