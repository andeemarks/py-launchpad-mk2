import time

from launchpad.launchpad import Launchpad
from launchpad.colour import RGBColour
from launchpad.coord import Coord

def coord_to_color(x: int, y: int) -> int:
    return (x * 8) + y

def do_to_grid(title: str, doer) -> None:
    print(title)
    for x in range(8):
        for y in range(8):
            doer(x, y)
    time.sleep(1)

lpad = Launchpad()

lpad.clear()

def colours1(x, y):
    lpad.cell_on(Coord(x,y), (y * 8) + x)

def colours2(x, y):
    lpad.cell_on(Coord(x,y), (y * 8) + x + 64)

def reds(x, y):
    lpad.cell_rgb(Coord(x,y), RGBColour.from_red(coord_to_color(x, y)))

def greens(x, y):
    lpad.cell_rgb(Coord(x,y), RGBColour.from_green(coord_to_color(x, y)))

def blues(x, y):
    lpad.cell_rgb(Coord(x,y), RGBColour.from_blue(coord_to_color(x, y)))

def yellows(x, y):
    lpad.cell_rgb(Coord(x,y), RGBColour.from_yellow(coord_to_color(x, y)))

def cyans(x, y):
    lpad.cell_rgb(Coord(x,y), RGBColour.from_cyan(coord_to_color(x, y)))

def magentas(x, y):
    lpad.cell_rgb(Coord(x,y), RGBColour.from_magenta(coord_to_color(x, y)))

def whites(x, y):
    lpad.cell_rgb(Coord(x,y), RGBColour.from_white(coord_to_color(x, y)))

do_to_grid("Showing colours 0-63...", colours1)
do_to_grid("Showing colours 64-127...", colours2)
do_to_grid("Showing reds by RGB...", reds)
do_to_grid("Showing greens by RGB...", greens)
do_to_grid("Showing blues by RGB...", blues)
do_to_grid("Showing yellows by RGB...", yellows)
do_to_grid("Showing cyans by RGB...", cyans)
do_to_grid("Showing magentas by RGB...", magentas)
do_to_grid("Showing whites by RGB...", whites)
