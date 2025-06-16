
class Coord():
    def __init__(self, x: int, y: int):
        if (0 <= x <= 8):
            self.x = x
        else:
            raise ValueError(f"x value of {x} is not within the range 0-8 inclusive")

        if (0 <= y <= 7):
            self.y = y 
        else:
            raise ValueError(f"y value of {y} is not within the range 0-7 inclusive")


    def to_offset(self) -> int: 
        return self.x + (10 * self.y)

    def __str__(self) -> str:
        return f"(x: {self.x}, y: {self.y})"

