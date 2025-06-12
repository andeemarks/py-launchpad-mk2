import mido
import random

NOTE_ON = 'note_on'
CHANNEL = 0
VELOCITY = 81
TIME = 0
FIRST_PAD = 10


def clear_grid(lpad):
    lpad.send(mido.Message('sysex', data=[240, 0, 32, 41, 2, 24, 14, 247]))

def cell_on(lpad, cell_offset):
    lpad.send(mido.Message(NOTE_ON, note=FIRST_PAD + cell_offset, channel=CHANNEL, velocity=random.randint(0, 127), time=TIME))

def cell_off(lpad, cell_offset):
    lpad.send(mido.Message(NOTE_ON, note=FIRST_PAD + cell_offset, channel=CHANNEL, velocity=0, time=TIME))

def cell_flash(lpad, cell_offset):
    lpad.send(mido.Message(NOTE_ON, note=FIRST_PAD + cell_offset, channel=CHANNEL+1, velocity=random.randint(0, 127), time=TIME))

def cell_pulse(lpad, cell_offset):
    lpad.send(mido.Message(NOTE_ON, note=FIRST_PAD + cell_offset, channel=CHANNEL+2, velocity=random.randint(0, 127), time=TIME))

lpad = mido.open_output('Launchpad MK2 MIDI 1')

for cell_offset in range(0, 9 * 9):
    cell_on(lpad, cell_offset)
    
for cell_offset in range(0, 9 * 9):
    cell_off(lpad, cell_offset)

for cell_offset in range(0, 9 * 9):
    cell_flash(lpad, cell_offset)

for cell_offset in range(0, 9 * 9):
    cell_pulse(lpad, cell_offset)

lpad.close()
