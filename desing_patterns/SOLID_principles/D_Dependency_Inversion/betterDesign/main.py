from Copy import Copy
from KeyboardReader import KeyboardReader
from ScreenWriter import ScreenWriter


if __name__ == "__main__":
    reader = KeyboardReader()
    writer = ScreenWriter()
    
    copy = Copy(reader, writer)
    copy.copy()
