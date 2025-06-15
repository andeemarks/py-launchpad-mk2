import mido

from .message import BasicMessage, FlashMessage, SysexMessage, PulseMessage
from .colour import Colour, RGBColour
from .pad import PadInput
from .coord import Coord

from enum import Enum

CHANNEL = 0
TIME = 0

class Row(Enum):
    1, 2, 3, 4, 5, 6, 7, 8

class Col(Enum):
    1, 2, 3, 4, 5, 6, 7, 8

class Launchpad():
    DEVICE_NAME = 'Launchpad MK2 MIDI 1'

    def __init__(self, input_handler_callback=None):
        self.output = mido.open_output(self.DEVICE_NAME)
        self.input = mido.open_input(self.DEVICE_NAME)
        self.input_handler_callback = input_handler_callback
        self.input.callback = self.handler

    def handler(self, message: mido.Message):
        if (self.input_handler_callback):
            self.input_handler_callback(PadInput(message))
        else: 
            print(message)

    def x_y_to_offset(self, x,y) -> int: 
        return x + (10 * y)

    def cell_on(self, coord: Coord, colour: Colour):
        self.output.send(BasicMessage(coord, colour))

    def cell_off(self, coord: Coord):
        self.output.send(BasicMessage(coord))

    def cell_flash(self, coord: Coord, colour: Colour):
        self.output.send(FlashMessage(coord, colour))

    def cell_pulse(self, coord: Coord, colour: Colour):
        self.output.send(PulseMessage(coord, colour))

    def clear(self):
        message = SysexMessage()
        message.data += (14, 0)
        self.output.send(message)

    def grid_on(self, colour: Colour):
        message = SysexMessage()
        message.data += (14, colour)
        self.output.send(message)

    def row_on(self, row: Row, colour: Colour):
        message = SysexMessage()
        message.data += (13, row, colour)
        self.output.send(message)

    def col_on(self, col: Col, colour: Colour):
        message = SysexMessage()
        message.data += (12, col, colour)
        self.output.send(message)

    def scroll_text(self, text: str, colour: Colour):
        message = SysexMessage()
        message.data += (20, colour, 0) + tuple([ord(ch) for ch in text])
        self.output.send(message)

    def loop_text(self, text: str, colour: Colour):
        message = SysexMessage()
        message.data += (20, colour, 1) + tuple([ord(ch) for ch in text])
        self.output.send(message)

    def loop_stop(self):
        message = SysexMessage()
        message.data += (20, )
        self.output.send(message)

    def cell_rgb(self, coord: Coord, rgb: RGBColour):
        message = SysexMessage()
        message.data += (11, 11 + coord.to_offset(), rgb.r, rgb.g, rgb.b)
        self.output.send(message)