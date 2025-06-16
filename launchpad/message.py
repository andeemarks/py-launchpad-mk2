import mido

from .coord import Coord

CHANNEL = 0
TIME = 0

class BasicMessage(mido.Message):
    FIRST_PAD = 11
    NOTE_ON = 'note_on'

    def __init__(self, coord: Coord, color=0, channel=CHANNEL):
        super().__init__(self.NOTE_ON,
                            note=self.FIRST_PAD + coord.to_offset(),
                            channel=channel,
                            velocity=color,
                            time=TIME)

class FlashMessage(BasicMessage):
    def __init__(self, coord: Coord, color=0):
        super().__init__(coord, color, channel=CHANNEL+1)

class PulseMessage(BasicMessage):
    def __init__(self, coord: Coord, color=0):
        super().__init__(coord, color, channel=CHANNEL+2)

class SysexMessage(mido.Message):
    SYSEX_HEADER = (0, 32, 41, 2, 24)
    SYSEX = 'sysex'

    def __init__(self):
        super().__init__(self.SYSEX, data=self.SYSEX_HEADER, time=TIME)
