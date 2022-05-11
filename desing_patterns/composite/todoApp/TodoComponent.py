"""
Interfaz que declara el comportamiento de un componente de la lista.
Analogo a Component.
"""
class TodoComponent:
    def isDone(self) -> bool:
        raise NotImplementedError