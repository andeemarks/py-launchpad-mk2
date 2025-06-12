import mido

class PadInput():
    def __init__(self, message: mido.Message):
        self.message = message

    def is_pad_down(self) -> bool:
        return self.message.velocity == 127
        
    def is_pad_up(self) -> bool:
        return self.message.velocity == 0

    def channel(self) -> int:
        return self.message.channel

    def note(self) -> int:
        return self.message.note

    def time(self) -> int:
        return self.message.time

    def x_y(self) -> (int, int):
        x = self.message.note % 10 - 1
        y = self.message.note // 10 - 1

        return (x, y)

    def __str__(self) -> str:
        return self.message.__str__()        