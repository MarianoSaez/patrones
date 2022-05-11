from AbstractFactory import AbstractFactory
from ProductA import ProductA
from ProductB import ProductB
from ProductAY import ProductAY
from ProductBY import ProductBY


class ConcreteFactoryY(AbstractFactory):
    def createProductA(self) -> ProductA:
        return ProductAY()

    def createProductB(self) -> ProductB:
        return ProductBY()
