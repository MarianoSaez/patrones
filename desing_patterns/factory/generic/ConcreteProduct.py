from IProduct import IProduct


class ConcreteProduct(IProduct):
    def someMethod(self) -> None:
        print("Soy un producto concreto!")
