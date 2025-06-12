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

def cell_on(lpad, cell_offset, color):
    lpad.send(mido.Message(NOTE_ON, note=FIRST_PAD + cell_offset, channel=CHANNEL, velocity=color, time=TIME))

def cell_off(lpad, cell_offset):
    lpad.send(mido.Message(NOTE_ON, note=FIRST_PAD + cell_offset, channel=CHANNEL, velocity=0, time=TIME))

def cell_flash(lpad, cell_offset, color):
    lpad.send(mido.Message(NOTE_ON, note=FIRST_PAD + cell_offset, channel=CHANNEL+1, velocity=color, time=TIME))

def cell_pulse(lpad, x, y, color):
    lpad.send(mido.Message(NOTE_ON, note=FIRST_PAD + coordinate_pair_to_index(x, y), channel=CHANNEL+2, velocity=color, time=TIME))

def coordinate_pair_to_index(x,y): 
    return x + (10 * y)

def clear_grid(lpad):
    lpad.send(mido.Message(SYSEX, data=SYSEX_HEADER + (14, 0), time=TIME))

def grid_on(lpad, color):
    lpad.send(mido.Message(SYSEX, data=SYSEX_HEADER + (14, color), time=TIME))

def row_on(lpad, row, color):
    lpad.send(mido.Message(SYSEX, data=SYSEX_HEADER + (13, row, color), time=TIME))

def col_on(lpad, col, color):
    lpad.send(mido.Message(SYSEX, data=SYSEX_HEADER + (12, col, color), time=TIME))

def scroll_text(lpad, text, color):
    lpad.send(mido.Message(SYSEX, data=SYSEX_HEADER + (20, color, 0) + tuple([ord(ch) for ch in text]), time=TIME))

def loop_text(lpad, text, color):
    lpad.send(mido.Message(SYSEX, data=SYSEX_HEADER + (20, color, 1) + tuple([ord(ch) for ch in text]), time=TIME))

def loop_stop(lpad):
    lpad.send(mido.Message(SYSEX, data=SYSEX_HEADER + (20, ), time=TIME))

def cell_rgb(lpad, x, y, r, g, b):
    lpad.send(mido.Message(SYSEX, data=SYSEX_HEADER + (11, coordinate_pair_to_index(x, y), r, g, b), time=TIME))

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
