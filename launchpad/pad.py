import mido

from .coord import Coord

class PadInput():
    def __init__(self, message: mido.Message):
        self.message = message

        try:
            self.velocity = message.velocity
        except AttributeError:
            self.velocity = 0

        try:
            self.channel = message.channel
        except AttributeError:
            self.channel = 0

        try:
            self.note = message.note
        except AttributeError:
            self.note = 0

        try:
            self.time = message.time
        except AttributeError:
            self.time = 0

        try:
            self.control = message.control
        except AttributeError:
            self.control = 0

        try:
            self.value = message.value
        except AttributeError:
            self.value = 0

    def is_cursor_down(self) -> bool:
        return self.control == 105

    def is_cursor_up(self) -> bool:
        return self.control == 104

    def is_cursor_left(self) -> bool:
        return self.control == 106

    def is_cursor_right(self) -> bool:
        return self.control == 107

    def is_cursor_key(self) -> bool:
        return self.control in [104, 105, 106, 107]

    def is_pad_down(self) -> bool:
        return (self.velocity == 127) | (self.value == 127)

    def is_pad_up(self) -> bool:
        return not self.is_pad_down()

    def x_y(self) -> Coord:
        if self.note > 0:
            x = self.note % 10 - 1
            y = self.note // 10 - 1

            return Coord(x, y)

        raise ValueError("Message has no note attribute")

    def __str__(self) -> str:
        return self.message.__str__()
