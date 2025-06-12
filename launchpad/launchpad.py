import mido

from .message import BasicMessage, FlashMessage, SysexMessage, PulseMessage

CHANNEL = 0
TIME = 0

class Launchpad():
    DEVICE_NAME = 'Launchpad MK2 MIDI 1'

    def __init__(self, input_handler_callback=None):
        self.output = mido.open_output(self.DEVICE_NAME)
        self.input = mido.open_input(self.DEVICE_NAME)
        self.input.callback = (input_handler_callback or self.handler)

    def handler(self, message):
        print(message)

    def coordinate_pair_to_index(self, x,y): 
        return x + (10 * y)

    def cell_on(self, cell_offset, color):
        self.output.send(BasicMessage(cell_offset, color))

    def cell_off(self, cell_offset):
        self.output.send(BasicMessage(cell_offset))

    def cell_flash(self, cell_offset, color):
        self.output.send(FlashMessage(cell_offset, color))

    def cell_pulse(self, cell_offset, color):
        self.output.send(PulseMessage(cell_offset, color))

    def clear(self):
        message = SysexMessage()
        message.data += (14, 0)
        self.output.send(message)

    def grid_on(self, color):
        message = SysexMessage()
        message.data += (14, color)
        self.output.send(message)

    def row_on(self, row, color):
        message = SysexMessage()
        message.data += (13, row, color)
        self.output.send(message)

    def col_on(self, col, color):
        message = SysexMessage()
        message.data += (12, col, color)
        self.output.send(message)

    def scroll_text(self, text, color):
        message = SysexMessage()
        message.data += (20, color, 0) + tuple([ord(ch) for ch in text])
        self.output.send(message)

    def loop_text(self, text, color):
        message = SysexMessage()
        message.data += (20, color, 1) + tuple([ord(ch) for ch in text])
        self.output.send(message)

    def loop_stop(self):
        message = SysexMessage()
        message.data += (20, )
        self.output.send(message)

    def cell_rgb(self, x, y, r, g, b):
        message = SysexMessage()
        message.data += (11, self.coordinate_pair_to_index(x, y), r, g, b)
        self.output.send(message)
