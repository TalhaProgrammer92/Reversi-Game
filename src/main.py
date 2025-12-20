from prototype.ansi.enums.foreground import Foreground
from prototype.ansi.enums.background import Background
from prototype.ansi.enums.style import Style
from prototype.ansi.color import *

if __name__ == '__main__':
    print(colored_text(
        text='Talha Ahmad',
        foreground=Foreground.BRIGHT_RED,
        background=Background.BLACK,
        style=Style.ITALIC
    ))
