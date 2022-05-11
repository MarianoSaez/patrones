class Writer:
    """
    Interfaz que declara el comportamiento que debe poseer un Writer
    que realiza operaciones de Output.
    """
    def write(self, string: str) -> None:
        raise NotImplementedError