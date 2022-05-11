from random import randint
from ConsoleLogger import ConsoleLogger
from ErrorLogger import ErrorLogger
from FileLogger import FileLogger


# Constantes
INFO_LVL = 0
ERROR_LVL = 1
FILE_LVL = 2


if __name__ == "__main__":
    # Instanciar manejadores de la cadena
    consoleLogger = ConsoleLogger()
    errorLogger = ErrorLogger()
    fileLogger = FileLogger()

    # Enlazar eslabones
    consoleLogger.setNxt(errorLogger)
    errorLogger.setNxt(fileLogger)

    # Enviar request a la cadena
    for r in [randint(0, 3) for i in range(10)]:
        consoleLogger.handleLog(r, f"[ {r} ] Algun mensaje...")
