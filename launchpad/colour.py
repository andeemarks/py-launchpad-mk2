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
    def white(cls, w: int):
        return cls(w, w, w)

    def __init__(self, r: int, g: int, b: int):
        if 0 > r >= 63:
            raise ValueError(f"red value ({r}) must be between 0 and 63 inclusive")
        if 0 > g >= 63:
            raise ValueError(f"green value ({g}) must be between 0 and 63 inclusive")
        if 0 > b >= 63:
            raise ValueError(f"blue value ({b}) must be between 0 and 63 inclusive")

        self.r = r
        self.g = g 
        self.b = b 

    @staticmethod
    def random_element() -> int:
        return random.randint(0, 63)
    