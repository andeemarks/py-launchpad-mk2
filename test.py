import mido

NOTE_ON = 'note_on'
CHANNEL = 0
VELOCITY = 81
TIME = 0
FIRST_PAD = 10

lpad = mido.open_output('Launchpad MK2 MIDI 1')
# lpad.send(mido.Message.from_bytes([0x90, 0x40, 0x60]))
for (pad_offset, color_offset) in zip(range(0, 9 * 9), range(0, 9 * 9)):
    lpad.send(mido.Message(NOTE_ON, note=FIRST_PAD + pad_offset, channel=CHANNEL, velocity=color_offset, time=TIME))

lpad.close()
