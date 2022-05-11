from ConcreteObservable import ConcreteObservable
from IObserver import IObserver


class ConcreteObserver(IObserver):
    def __init__(self, id: int, observable: ConcreteObservable) -> None:
        super().__init__()
        self.id = id
        self.observable = observable

    def update(self):
        state = self.observable.getState()
        print(f"[Observer {self.id}] El nuevo estado es: {state}")
