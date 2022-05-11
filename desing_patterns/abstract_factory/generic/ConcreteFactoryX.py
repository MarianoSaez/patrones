from AbstractFactory import AbstractFactory
from ProductA import ProductA
from ProductB import ProductB
from ProductAX import ProductAX
from ProductBX import ProductBX


class ConcreteFactoryX(AbstractFactory):
    def createProductA(self) -> ProductA:
        return ProductAX()

    def createProductB(self) -> ProductB:
        return ProductBX()
