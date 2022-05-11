# Pattern imports
from LinuxUIFactory import LinuxUIFactory
from MacUIFactory import MacUIFactory
from WinUIFactory import WinUIFactory

# Example imports
from platform import system

OS = system()

# Determinar el tipo de factory en base a algun parametro (OS)
if OS == "Linux":
    factory = LinuxUIFactory()
elif OS == "Darwin":
    factory = MacUIFactory()
else:
    factory = WinUIFactory()
    