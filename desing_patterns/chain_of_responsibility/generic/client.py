from ConcreteHandler1 import ConcreteHandler1
from ConcreteHandler2 import ConcreteHandler2
from ConcreteHandler3 import ConcreteHandler3

if __name__ == "__main__":
    # Instanciamos los manejadores de la cadena
    ch1 = ConcreteHandler1()
    ch2 = ConcreteHandler2()
    ch3 = ConcreteHandler3()

    # Enlazamos la cadena segun algun criterio u orden
    ch1.setNext(ch2)
    ch2.setNext(ch3)

    # Enviamos algunos request a la cadena
    for r in range(0, 50, 10):
        ch1.handle(r)
