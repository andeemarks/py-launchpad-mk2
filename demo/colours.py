import time

from launchpad.launchpad import Launchpad
from launchpad.pad import PadInput
from launchpad.colour import Colour
from launchpad.coord import Coord

def input_handler(message: PadInput):
    coord: Coord = message.x_y()
    lpad.scroll_text(f'{(coord.y * 8) + coord.x}', Colour.WHITE)

lpad = Launchpad(input_handler)

lpad.clear()

print("Showing colours 0-63...")
for x in range(8):
    for y in range(8):
        lpad.cell_on(Coord(x,y), (y * 8) + x)

time.sleep(2)

print("Showing colours 64-127...")
for x in range(8):
    for y in range(8):
        lpad.cell_on(Coord(x,y), (y * 8) + x + 64)

try:
    while (True):
        pass
except KeyboardInterrupt:
    print("Thanks for coming!")
    exit()