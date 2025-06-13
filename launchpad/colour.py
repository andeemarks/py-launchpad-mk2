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

    @staticmethod
    def random_rgb_element():
        return random.randint(0, 63)
    