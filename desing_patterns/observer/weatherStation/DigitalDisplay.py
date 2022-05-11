from IObserver import IObserver
from WeatherStation import WeatherStation


class DigitalDisplay(IObserver):
    def __init__(self, weatherStation: WeatherStation) -> None:
        super().__init__()
        self.weatherStation = weatherStation

    def update(self) -> None:
        temp = self.weatherStation.getTemperature()
        print(f"[ Digital Station ] {temp} grados")