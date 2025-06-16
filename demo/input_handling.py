import time

from launchpad.launchpad import Launchpad
from launchpad.coord import Coord
from launchpad.pad import PadInput
from launchpad.colour import Colour

coord: Coord = None

def input_handler(message: PadInput):
    if (message.is_pad_up()): # only handling a single message in a pad down/pad up sequence
        return

    lpad.clear()

    global coord

    if (message.is_cursor_key()):
        try:
            if message.is_cursor_down():   
                coord = Coord(coord.x, coord.y - 1)
            elif message.is_cursor_up():   
                coord = Coord(coord.x, coord.y + 1)
            elif message.is_cursor_left():   
                coord = Coord(coord.x - 1, coord.y)
            elif message.is_cursor_right():   
                coord = Coord(coord.x + 1, coord.y)
        except ValueError:
            pass # we'll silently fail/continue when reaching the end of the grid
    else:
        coord = message.x_y()

    print(coord)
    lpad.cell_on(coord, Colour.WHITE)

lpad = Launchpad(input_handler)

lpad.clear()

try:
    while (True):
        pass
except KeyboardInterrupt:
    print("Thanks for coming!")
    exit()