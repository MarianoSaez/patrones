class Reader:
    """
    Interfaz que declara el comportamiento que debe poseer un Reader
    que realiza operaciones de Input.
    """
    def read(self) -> str:
        raise NotImplementedError