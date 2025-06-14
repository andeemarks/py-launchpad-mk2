
class Coord():
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y 

    def to_offset(self) -> int: 
        return self.x + (10 * self.y)

