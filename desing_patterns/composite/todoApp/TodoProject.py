"""
Implementa el comportamiento de un objeto complejo/con hijos.
Propaga y recolecta resultados de los hijos y eleva el resultado
conjunto.
Analogo a Composite.
"""
from TodoComponent import TodoComponent


class TodoProject(TodoComponent):
    def __init__(self, components: list[TodoComponent]) -> None:
        self.components = components
        self.done = False

    def isDone(self) -> bool:
        projectDone = True
        for comp in self.components:
            projectDone &= comp.isDone() # Realizar una operacion AND

        self.done = projectDone

        return self.done

    def addComp(self, comp: TodoComponent) -> None:
        self.components.append(comp)

    def removeComp(self, comp: TodoComponent) -> None:
        self.components.remove(comp)
