import random

class Colour:
    @staticmethod
    def random():
        return random.randint(0, 127)

    @staticmethod
    def random_rgb_element():
        return random.randint(0, 63)
    