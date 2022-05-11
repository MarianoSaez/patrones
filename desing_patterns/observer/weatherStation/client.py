from WeatherStation import WeatherStation
from WebDisplay import WebDisplay
from DigitalDisplay import DigitalDisplay


if __name__ == "__main__":
    # Instanciar un sujeto observable
    weatherStation = WeatherStation(24)

    # Instanciar observadores
    digitalDisplay = DigitalDisplay(weatherStation)
    webDisplay = WebDisplay(weatherStation)

    # Suscribir observadores al cambio de estado de temperatura
    weatherStation.addObserver(digitalDisplay)
    weatherStation.addObserver(webDisplay)

    # Modificar la tempratura
    temps = [25, 27, 30, 28, 16]
    for temp in temps:
        weatherStation.setTemperature(temp)
