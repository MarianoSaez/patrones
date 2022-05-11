from IObservable import IObservable
from IObserver import IObserver


class ConcreteObservable(IObservable):
    def __init__(self, state: int = 0, observers: list[IObserver] = []) -> None:
        super().__init__()
        self.state = state
        self.observers = observers

    # Metodos de la interfaz IObservable

    def add(self, observer: IObserver) -> None:
        self.observers.append(observer)

    def remove(self, observer: IObserver) -> None:
        self.observers.remove(observer)

    def notify(self) -> None:
        for observer in self.observers:
            observer.update()


    # Metodos de la clase ConcreteObservable

    def setState(self, state: int) -> None:
        self.state = state
        self.notify()   # Notificar el cambio a los observadores

    def getState(self) -> int:
        return self.state
