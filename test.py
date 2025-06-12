import random
import time

from launchpad.launchpad import Launchpad

BRIGHT_MAX = 63

lpad = Launchpad()
for cell_offset in range(0, 9 * 9):
    lpad.cell_on(cell_offset, random.randint(0, 127))

time.sleep(1)

for cell_offset in range(0, 9 * 9):
    lpad.cell_flash(cell_offset, random.randint(0, 127))

time.sleep(1)

for cell_offset in range(0, 9 * 9):
    lpad.cell_pulse(cell_offset, random.randint(0, 127))

time.sleep(1)

for cell_offset in range(0, 9 * 9):
    lpad.cell_off(cell_offset)

time.sleep(1)

lpad.grid_on(random.randint(0, 127))

time.sleep(1)

lpad.row_on(3, random.randint(0, 127))

time.sleep(1)

lpad.col_on(5, random.randint(0, 127))

time.sleep(1)

lpad.scroll_text("Andy", random.randint(0, 127))

time.sleep(1)

lpad.loop_text("rocks!", random.randint(0, 127))

time.sleep(1)

lpad.loop_stop()

time.sleep(1)

lpad.clear_grid()

lpad.cell_rgb(6, 2, BRIGHT_MAX, BRIGHT_MAX, 0)

time.sleep(1)

lpad.clear_grid()
