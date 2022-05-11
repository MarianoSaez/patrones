# Instance imports
from CopyForever import CopyForever
from KeyboardReader import KeyboardReader
from ScreenWriter import ScreenWriter

# Type imports
from Copy import Copy
from Reader import Reader
from Writer import Writer


class App:
    def __init__(self, copier: Copy, reader: Reader, writer: Writer) -> None:
        self.reader = reader
        self.writer = writer
        self.copier = copier
    
    def run(self):
        self.copier.copy()


if __name__ == "__main__":
    reader = KeyboardReader()
    writer = ScreenWriter()
    copy =  CopyForever(reader, writer)
    
    
    app = App(copy, reader, writer)
    app.run()
