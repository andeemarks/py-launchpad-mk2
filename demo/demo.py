import time

from launchpad.launchpad import Launchpad
from launchpad.coord import Coord
from launchpad.colour import Colour, RGBColour

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
        lpad.cell_flash(Coord(0, y), 60)
        lpad.cell_flash(Coord(7, y), 60)
    for x in range(8):
        lpad.cell_flash(Coord(x, 0), 60)
        lpad.cell_flash(Coord(x, 7), 60)

def pulse_middle():
    for x in range(1, 7):
        for y in range(1, 7):
            lpad.cell_pulse(Coord(x, y), 60)
    time.sleep(1)

def brightness_quadrants():
    for x in range(0, 4):
        for y in range (0, 4):
            brightness = ((4 * y) + x) * 4
            lpad.cell_rgb(Coord(x, y), RGBColour.from_red(brightness))
            lpad.cell_rgb(Coord(x + 4, y), RGBColour.from_green(brightness))
            lpad.cell_rgb(Coord(x, y + 4), RGBColour.from_blue(brightness))
            lpad.cell_rgb(Coord(x + 4, y + 4), RGBColour.from_white(brightness))
    time.sleep(2)

lpad = Launchpad()

lpad.clear()
wipe_left_to_right()
wipe_top_to_bottom()
flash_border()
pulse_middle()
lpad.clear()
brightness_quadrants()
lpad.scroll_text("Touch me!", Colour.GREEN)
