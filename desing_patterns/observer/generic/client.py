from ConcreteObservable import ConcreteObservable
from ConcreteObserver import ConcreteObserver


if __name__ == "__main__":
    # Instanciar un sujeto observable
    concreteObservable = ConcreteObservable()

    # Instanciar observadores y pasar referencia del observable
    concreteObserver1 = ConcreteObserver(1, concreteObservable)
    concreteObserver2 = ConcreteObserver(2, concreteObservable)

    # Suscribir a los observadores para ser notificados
    concreteObservable.add(concreteObserver1)
    concreteObservable.add(concreteObserver2)

    # Modificar estado en observable
    for i in range(1, 10):
        concreteObservable.setState(i)
