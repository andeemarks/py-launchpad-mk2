from datetime import datetime

from launchpad.launchpad import Launchpad

lpad = Launchpad()

lpad.clear()

lpad.scroll_text(datetime.now().strftime("%H:%M:%S"), 34)
