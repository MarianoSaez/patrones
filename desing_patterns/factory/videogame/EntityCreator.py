"""
Interfaz que declara el metodo para la creacion de entidades.
Analogo a ICreator.
"""
from Entity import Entity


class EntityCreator:
    def createEntity(self) -> Entity:
        raise NotImplementedError
