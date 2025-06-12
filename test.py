import time

from launchpad.launchpad import Launchpad
from launchpad.colour import BRIGHT_MAX, random_colour

def pause():
    time.sleep(1)


def input_handler(message):
    print(f'input: {message}')

lpad = Launchpad(input_handler)
for cell_offset in range(0, 9 * 9):
    lpad.cell_on(cell_offset, random_colour())

pause()

for cell_offset in range(0, 9 * 9):
    lpad.cell_flash(cell_offset, random_colour())

pause()

for cell_offset in range(0, 9 * 9):
    lpad.cell_pulse(cell_offset, random_colour())

pause()

for cell_offset in range(0, 9 * 9):
    lpad.cell_off(cell_offset)

pause()

lpad.grid_on(random_colour())

pause()

lpad.row_on(3, random_colour())

pause()

lpad.col_on(5, random_colour())

pause()

lpad.scroll_text("Andy", random_colour())

pause()

lpad.loop_text("rocks!", random_colour())

pause()

lpad.loop_stop()

pause()

lpad.clear()

lpad.cell_rgb(6, 2, BRIGHT_MAX, BRIGHT_MAX, 0)

pause()

lpad.clear()
