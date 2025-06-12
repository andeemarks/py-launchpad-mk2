import time

from launchpad.launchpad import Launchpad
from launchpad.colour import Colour

def pause():
    time.sleep(1)


def input_handler(message):
    print(f'input: {message}')

lpad = Launchpad(input_handler)
for cell_offset in range(0, 9 * 9):
    lpad.cell_on(cell_offset, Colour.random())

pause()

for cell_offset in range(0, 9 * 9):
    lpad.cell_flash(cell_offset, Colour.random())

pause()

for cell_offset in range(0, 9 * 9):
    lpad.cell_pulse(cell_offset, Colour.random())

pause()

for cell_offset in range(0, 9 * 9):
    lpad.cell_off(cell_offset)

pause()

lpad.grid_on(Colour.random())

pause()

lpad.row_on(3, Colour.random())

pause()

lpad.col_on(5, Colour.random())

pause()

lpad.scroll_text("Andy", Colour.random())

pause()

lpad.loop_text("rocks!", Colour.random())

pause()

lpad.loop_stop()

pause()

lpad.clear()

lpad.cell_rgb(6, 2, Colour.random_rgb_element(), Colour.random_rgb_element(), Colour.random_rgb_element())

pause()

lpad.clear()
