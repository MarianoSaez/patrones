from ConcreteFactoryX import ConcreteFactoryX
from ConcreteFactoryY import ConcreteFactoryY
from ProductA import ProductA
from ProductB import ProductB



if __name__ == "__main__":
    print("1. Fabrica X")
    print("2. Fabrica Y")
    i = input("Ingrese [1, 2]: ")


    # Determinar que fabrica se instanciara
    if i == "1":
        factory = ConcreteFactoryX()
    else:
        factory = ConcreteFactoryY()

    # Obtener instancias de productos a traves de los metodos de la fabricas
    prodA: ProductA = factory.createProductA()
    prodB: ProductB = factory.createProductB()

    # Utilizar los productos
    prodA.someMethodA()
    prodB.someMethodB()
