from jinja2 import TemplateRuntimeError
from ISubject import ISubject
from IObserver import IObserver


class WeatherStation(ISubject):
    def __init__(self, temperature: int = 24, observers: list[IObserver] = []) -> None:
        super().__init__()
        self.observers = observers
        self.temperature = temperature

    # Metodos de la interfaz ISubject
    
    def addObserver(self, observer: IObserver) -> None:
        self.observers.append(observer)

    def removeObserver(self, observer: IObserver) -> None:
        self.observers.remove(observer)

    def notify(self) -> None:
        for observer in self.observers:
            observer.update()
    
    # Metodos de WeatherStation

    def setTemperature(self, temperature: int) -> None:
        self.temperature = temperature
        self.notify()   # Notificar a los observadores

    def getTemperature(self) -> int:
        return self.temperature