from io import IOBase
from typing import IO
from IObserver import IObserver
from WeatherStation import WeatherStation


class WebDisplay(IObserver):
    def __init__(self, weatherStation: WeatherStation) -> None:
        super().__init__()
        self.weatherStation = weatherStation

    def update(self) -> None:
        temp = self.weatherStation.getTemperature()
        print(f"[ WebDisplay ] <div><p>Temperatura: {temp}</p></div>")