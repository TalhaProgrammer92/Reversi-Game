from prototype.ansi.enums.foreground import Foreground
from prototype.ansi.enums.background import Background
from prototype.ansi.enums.style import Style
from prototype.ansi.color import Decoration
from prototype.text.menu import Menu
from prototype.text.text import Text

if __name__ == '__main__':
    menu: Menu = Menu(
        title=Text(
            text='Main Menu',
            decoration=Decoration(
                foreground=Foreground.BRIGHT_MAGENTA,
                style=Style.BOLD
            )
        ),
        title_decorator='*',
        options_decoration=Decoration(
            foreground=Foreground.BRIGHT_CYAN
        )
    )
    menu.addOption('New Game')
    menu.addOption('Load Game')
    menu.addOption('Settings')
    menu.addOption('Credits')
    menu.addOption('Exit')

    menu.display()
