import time

from launchpad.launchpad import Launchpad
from launchpad.pad import PadInput
from launchpad.colour import Colour

def input_handler(message: PadInput):
    (x, y) = message.x_y()
    lpad.cell_on(x + (10 * y), Colour.WHITE)

def wipe_left_to_right():
    for x in range(8):
        lpad.col_on(x, 66)
        time.sleep(0.2)
        lpad.col_on(x, 0)

def wipe_top_to_bottom():
    for y in range(8):
        lpad.row_on(y, 66)
        time.sleep(0.2)

def flash_border():
    for y in range(8):
        lpad.cell_flash(0 * 10 + y, 60)
        lpad.cell_flash(7 * 10 + y, 60)
    for x in range(8):
        lpad.cell_flash(x * 10 + 0, 60)
        lpad.cell_flash(x * 10 + 7, 60)

def pulse_middle():
    for x in range(1, 7):
        for y in range(1, 7):
            lpad.cell_pulse(x * 10 + y, 60)
    time.sleep(1)

def brightness_quadrants():
    for x in range(0, 4):
        for y in range (0, 4):
            brightness = ((4 * y) + x) * 4
            lpad.cell_rgb(x, y, brightness, 0, 0)
            lpad.cell_rgb(x + 4, y, 0, brightness, 0)
            lpad.cell_rgb(x, y + 4, 0, 0, brightness)
            lpad.cell_rgb(x + 4, y + 4, brightness, brightness, brightness)
    time.sleep(2)

lpad = Launchpad(input_handler)

lpad.clear()
wipe_left_to_right()
wipe_top_to_bottom()
flash_border()
pulse_middle()
lpad.clear()
brightness_quadrants()
lpad.scroll_text("Touch me!", Colour.GREEN)
lpad.clear()
while (True):
    pass