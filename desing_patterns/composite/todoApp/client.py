from TodoItem import TodoItem
from TodoProject import TodoProject


if __name__ == "__main__":
    # Instanciar algunos componentes
    item1 = TodoItem()
    item2 = TodoItem()
    item3 = TodoItem()
    item4 = TodoItem()
    item5 = TodoItem()
    item6 = TodoItem()

    proj1 = TodoProject([])
    proj2 = TodoProject([])
    root = TodoProject([])

    # Componer estructura
    root.addComp(item1)
    root.addComp(item2)
    root.addComp(proj1)
    root.addComp(proj2)

    proj1.addComp(item3)
    proj1.addComp(item4)

    proj2.addComp(item5)
    proj2.addComp(item6)

    """
    Estructura del arbol:

    root
    |
    |___item1 - Hecho
    |
    |___item2
    |
    |___proj1
    |   |___item3 - Hecho
    |   |___item4
    |
    |___proj2
        |___item5 - Hecho
        |___item6 - Hecho
    """

    # "Completar" algunas tareas
    item1.setDone(True)
    # item2.setDone(True)
    item3.setDone(True)
    # item4.setDone(True)
    item5.setDone(True)
    item6.setDone(True)

    # Interactuar con la estructura
    allDone = root.isDone()
    print(allDone)
