# Pattern imports
from EntityCreator import EntityCreator
from Entity import Entity
from Goomba import Goomba

# Logic imports
from random import randint

class EasyGoombaCreator(EntityCreator):
    """
    Fabrica encargada de crear Goombas de bajo nivel.
    """
    def createEntity(self) -> Entity:
        return Goomba(randint(1, 5), 0, 0)

class HardGoombaCreator(EntityCreator):
    """
    Fabrica encargada de crear Goombas de alto nivel.
    """
    def createEntity(self) -> Entity:
        return Goomba(randint(5, 10), 0, 0)

class RandomGoombaCreator(EntityCreator):
    """
    Fabrica encargada de crear Goombas de nivel random.
    """
    def createEntity(self) -> Entity:
        return Goomba(randint(1, 10), 0, 0)