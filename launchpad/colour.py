import random
from enum import IntEnum

class Colour(IntEnum):
    RED = 5
    BLUE = 45
    GREEN = 21
    WHITE = 3
    YELLOW = 13

    @staticmethod
    def random():
        return random.randint(0, 127)

class RGBColour():
    @classmethod
    def from_white(cls, white: int):
        return cls(white, white, white)

    @classmethod
    def from_red(cls, red: int):
        return cls(red, 0, 0)

    @classmethod
    def from_green(cls, green: int):
        return cls(0, green, 0)

    @classmethod
    def from_blue(cls, blue: int):
        return cls(0, 0, blue)

    @classmethod
    def from_cyan(cls, colour: int):
        return cls(0, colour, colour)

    @classmethod
    def from_yellow(cls, colour: int):
        return cls(colour, colour, 0)

    @classmethod
    def from_magenta(cls, colour: int):
        return cls(colour, 0, colour)

    def __init__(self, red: int, green: int, blue: int):
        if 0 > red >= 63:
            raise ValueError(f"red value ({red}) must bluee blueetween 0 and 63 inclusive")
        if 0 > green >= 63:
            raise ValueError(f"greenreen value ({green}) must bluee blueetween 0 and 63 inclusive")
        if 0 > blue >= 63:
            raise ValueError(f"bluelue value ({blue}) must bluee blueetween 0 and 63 inclusive")

        self.red = red
        self.green = green
        self.blue = blue

    @staticmethod
    def random_element() -> int:
        return random.randint(0, 63)
