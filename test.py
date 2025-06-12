import mido
import random
import time

NOTE_ON = 'note_on'
SYSEX = 'sysex'

CHANNEL = 0
VELOCITY = 81
TIME = 0
FIRST_PAD = 11
SYSEX_HEADER = (0, 32, 41, 2, 24)
BRIGHT_MAX = 63

class BasicMessage(mido.Message):
    def __init__(self, offset, color=0, channel=CHANNEL):
        super().__init__(NOTE_ON, note=FIRST_PAD + offset, channel=channel, velocity=color, time=TIME)

class FlashMessage(BasicMessage):
    def __init__(self, offset, color=0):
        super().__init__(offset, color, channel=CHANNEL+1)

class PulseMessage(BasicMessage):
    def __init__(self, offset, color=0):
        super().__init__(offset, color, channel=CHANNEL+2)

class SysexMessage(mido.Message):
    def __init__(self):
        super().__init__(SYSEX, data=SYSEX_HEADER, time=TIME)

def cell_on(lpad, cell_offset, color):
    lpad.send(BasicMessage(cell_offset, color))

def cell_off(lpad, cell_offset):
    lpad.send(BasicMessage(cell_offset))

def cell_flash(lpad, cell_offset, color):
    lpad.send(FlashMessage(cell_offset, color))

def cell_pulse(lpad, x, y, color):
    lpad.send(PulseMessage(cell_offset, color))

def coordinate_pair_to_index(x,y): 
    return x + (10 * y)

def clear_grid(lpad):
    message = SysexMessage()
    message.data += (14, 0)
    lpad.send(message)

def grid_on(lpad, color):
    message = SysexMessage()
    message.data += (14, color)
    lpad.send(message)

def row_on(lpad, row, color):
    message = SysexMessage()
    message.data += (13, row, color)
    lpad.send(message)

def col_on(lpad, col, color):
    message = SysexMessage()
    message.data += (12, col, color)
    lpad.send(message)

def scroll_text(lpad, text, color):
    message = SysexMessage()
    message.data += (20, color, 0) + tuple([ord(ch) for ch in text])
    lpad.send(message)

def loop_text(lpad, text, color):
    message = SysexMessage()
    message.data += (20, color, 1) + tuple([ord(ch) for ch in text])
    lpad.send(message)

def loop_stop(lpad):
    message = SysexMessage()
    message.data += (20, )
    lpad.send(message)

def cell_rgb(lpad, x, y, r, g, b):
    message = SysexMessage()
    message.data += (11, coordinate_pair_to_index(x, y), r, g, b)
    lpad.send(message)

lpad = mido.open_output('Launchpad MK2 MIDI 1')

for cell_offset in range(0, 9 * 9):
    cell_on(lpad, cell_offset, random.randint(0, 127))

time.sleep(1)

for cell_offset in range(0, 9 * 9):
    cell_flash(lpad, cell_offset, random.randint(0, 127))

time.sleep(1)

for x in range(0, 8):
    for y in range(0, 8):
        cell_pulse(lpad, x, y, random.randint(0, 127))

time.sleep(1)

for cell_offset in range(0, 9 * 9):
    cell_off(lpad, cell_offset)

time.sleep(1)

grid_on(lpad, random.randint(0, 127))

time.sleep(1)

row_on(lpad, 3, random.randint(0, 127))

time.sleep(1)

col_on(lpad, 5, random.randint(0, 127))

time.sleep(1)

scroll_text(lpad, "Andy", random.randint(0, 127))

time.sleep(1)

loop_text(lpad, "rocks!", random.randint(0, 127))

time.sleep(1)

loop_stop(lpad)

time.sleep(1)

clear_grid(lpad)
cell_rgb(lpad, 6, 2, BRIGHT_MAX, BRIGHT_MAX, 0)

lpad.close()
