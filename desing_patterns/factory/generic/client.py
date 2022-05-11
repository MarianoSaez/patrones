from ConcreteCreator import ConcreteCreator


if __name__ == "__main__":
    # Instanciamos una fabrica
    factory = ConcreteCreator()

    # Buscamos obtener una instancia de producto mediante la fabrica
    product = factory.factoryMethod()

    # Consumimos el producto
    product.someMethod()
