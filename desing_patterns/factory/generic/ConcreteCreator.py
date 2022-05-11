from ICreator import ICreator
from IProduct import IProduct
from ConcreteProduct import ConcreteProduct

class ConcreteCreator(ICreator):
    def factoryMethod(self) -> IProduct:
        return ConcreteProduct()