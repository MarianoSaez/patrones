from ProductA import ProductA
from ProductB import ProductB


class AbstractFactory:
    def createProductA(self) -> ProductA:
        raise NotImplementedError

    def createProductB(self) -> ProductB:
        raise NotImplementedError
