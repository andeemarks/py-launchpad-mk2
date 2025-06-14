from datetime import datetime

from launchpad.launchpad import Launchpad
from launchpad.pad import PadInput
from launchpad.colour import Colour
from launchpad.coord import Coord

def input_handler(message: PadInput):
    coord: Coord = message.x_y()
    lpad.scroll_text(f'{(coord.y * 8) + coord.x}', Colour.WHITE)

lpad = Launchpad(input_handler)

lpad.clear()

for x in range(10):
    for y in range(10):
        lpad.cell_on(Coord(x,y), Colour.random())

while (True):
    pass
