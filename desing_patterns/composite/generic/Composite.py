from Component import Component


class Composite(Component):
    def __init__(self, value: int, components: list[Component]) -> None:
        self.components = components
        self.value = value

    def addComp(self, component: Component) -> None:
        self.components.append(component)

    def removeComp(self, component: Component) -> None:
        self.components.remove(component)

    def operation(self) -> int:
        print(f"[ {type(self)} ]: Operacion sobre mi y mis componentes")
        val: int = self.value
        for comp in self.components:
            val += comp.operation()
        
        return val

