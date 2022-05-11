from Reader import Reader
from Writer import Writer


class Copy:
    def __init__(self, reader: Reader, writer: Writer) -> None:
        self.reader = reader
        self.writer = writer

    def copy(self) -> None:
        while (c := self.reader.read()) != "^":
            self.writer.write(c)
