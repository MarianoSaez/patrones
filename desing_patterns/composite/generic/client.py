from Component import Component
from Composite import Composite
from Leaf import Leaf


if __name__ == "__main__":
    # Instanciamos componentes del arbol
    root = Composite(10, [])
    c1 = Composite(5, [])
    l1 = Leaf(2)
    l2 = Leaf(3)
    l3 = Leaf(1)

    # Construir la estructura de arbol
    c1.addComp(l2)
    c1.addComp(l3)
    
    root.addComp(c1)
    root.addComp(l1)



    # Interactuar con la raiz del la estrutura
    result = root.operation()
    print("El resultado de sumar todos los valores del arbol es: ", result)
