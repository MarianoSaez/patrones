from ConcreteCreators import (
    EasyGoombaCreator,
    HardGoombaCreator,
    RandomGoombaCreator
)


if __name__ == "__main__":
    # Instanciar fabricas segun algun criterio
    print("1. Crear Goombas de bajo nivel")
    print("2. Crear Goombas de alto nivel")
    print("3. Crear Goombas de nivel aleatorio")
    select = input("Ingrese algun modo de creacion [1, 2, 3]: ")
    if select == 1:
        factory = EasyGoombaCreator()
    elif select == 2:
        factory = HardGoombaCreator()
    else:
        factory = RandomGoombaCreator()

    # Instanciamos una entidad con la fabrica seleccionada
    entity = factory.createEntity()

    # Consumimos metodos y atributos de la entidad
    entity.move(10, -25)
