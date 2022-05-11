from Copy import Copy


class CopyForever(Copy):
    def copy(self) -> None:
        while (c := self.reader.read()) != "^":
            self.writer.write(c)