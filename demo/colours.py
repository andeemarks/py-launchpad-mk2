from datetime import datetime

from launchpad.launchpad import Launchpad
from launchpad.pad import PadInput
from launchpad.colour import Colour

def input_handler(message: PadInput):
    (x, y) = message.x_y()
    lpad.scroll_text(f'{(y * 8) + x}', Colour.WHITE)

lpad = Launchpad(input_handler)

lpad.clear()

for cell_offset in range(0, 9 * 9):
    lpad.cell_on(cell_offset, cell_offset)

while (True):
    pass
