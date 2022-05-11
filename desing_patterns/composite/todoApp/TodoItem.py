"""
Implementa el comportamiento de un objecto primitivo/sin hijos.
Analogo a Leaf.
"""
from TodoComponent import TodoComponent


class TodoItem(TodoComponent):
    def __init__(self) -> None:
        self.done = False

    def isDone(self) -> bool:
        return self.done

    def setDone(self, done: bool) -> None:
        self.done = done
