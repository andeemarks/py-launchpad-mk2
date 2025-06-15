import time

from launchpad.launchpad import Launchpad
from launchpad.pad import PadInput
from launchpad.colour import Colour, RGBColour
from launchpad.coord import Coord

def coord_to_color(x: int, y: int) -> int:
    return (x * 8) + y

lpad = Launchpad()

lpad.clear()

print("Showing colours 0-63...")
for x in range(8):
    for y in range(8):
        lpad.cell_on(Coord(x,y), (y * 8) + x)

time.sleep(1)

print("Showing colours 64-127...")
for x in range(8):
    for y in range(8):
        lpad.cell_on(Coord(x,y), (y * 8) + x + 64)

time.sleep(1)

print("Showing reds by RGB...")
for x in range(8):
    for y in range(8):
        lpad.cell_rgb(Coord(x,y), RGBColour(coord_to_color(x, y), 0, 0))

time.sleep(1)

print("Showing greens by RGB...")
for x in range(8):
    for y in range(8):
        lpad.cell_rgb(Coord(x,y), RGBColour(0, coord_to_color(x, y), 0))

time.sleep(1)

print("Showing blues by RGB...")
for x in range(8):
    for y in range(8):
        lpad.cell_rgb(Coord(x,y), RGBColour(0, 0, coord_to_color(x, y)))

time.sleep(1)

print("Showing yellows by RGB...")
for x in range(8):
    for y in range(8):
        lpad.cell_rgb(Coord(x,y), RGBColour(coord_to_color(x, y), coord_to_color(x, y), 0))

time.sleep(1)

print("Showing cyans by RGB...")
for x in range(8):
    for y in range(8):
        lpad.cell_rgb(Coord(x,y), RGBColour(0, coord_to_color(x, y), coord_to_color(x, y)))

time.sleep(1)

print("Showing magentas by RGB...")
for x in range(8):
    for y in range(8):
        lpad.cell_rgb(Coord(x,y), RGBColour(coord_to_color(x, y), 0, coord_to_color(x, y)))

time.sleep(1)

print("Showing whites by RGB...")
for x in range(8):
    for y in range(8):
        lpad.cell_rgb(Coord(x,y), RGBColour.white(coord_to_color(x, y)))


