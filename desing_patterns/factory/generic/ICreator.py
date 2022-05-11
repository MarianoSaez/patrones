from IProduct import IProduct


class ICreator:
    def factoryMethod(self) -> IProduct:
        raise NotImplementedError
