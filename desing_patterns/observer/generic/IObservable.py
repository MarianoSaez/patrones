from IObserver import IObserver


class IObservable:
    def add(self, observer: IObserver):
        raise NotImplementedError

    def remove(self, observer: IObserver):
        raise NotImplementedError

    def notify(self):
        raise NotImplementedError