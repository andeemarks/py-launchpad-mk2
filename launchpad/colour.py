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
    def __init__(self, r: int, g: int, b: int):
        self.r = r
        self.g = g 
        self.b = b 

    @staticmethod
    def random_element() -> int:
        return random.randint(0, 63)
    