from prototype.ansi.enums.foreground import Foreground
from prototype.ansi.enums.background import Background
from prototype.ansi.enums.style import Style
from prototype.ansi.color import Decoration
from prototype.text.text import Text

menu_settings: dict = {
    'title': {
        'main-menu': Text(text='Main Menu', decoration=Decoration(
            foreground=Foreground.BRIGHT_CYAN,
            style=Style.BOLD
        ))
    },
    'title-decorator': {
        'main-menu': '='
    },
    'options-decoration': {
        'main-menu': Decoration(
            foreground=Foreground.BRIGHT_YELLOW,
            style=Style.ITALIC
        )
    }
}

message_settings: dict = {
    'text': {
        'info': '[INFO]',
        'success': '[SUCCESS]',
        'warning': '[WARNING]',
        'error': '[ERROR]'
    },
    'decoration': {
        'info': Decoration(
            foreground=Foreground.BRIGHT_CYAN,
            style=Style.BOLD
        ),
        'success': Decoration(
            foreground=Foreground.BRIGHT_GREEN,
            style=Style.BOLD
        ),
        'warning': Decoration(
            foreground=Foreground.BRIGHT_YELLOW,
            style=Style.BOLD
        ),
        'error': Decoration(
            foreground=Foreground.BRIGHT_RED,
            style=Style.BOLD
        )
    }
}

text_settings: dict = {
    'decoration': {
        'prompt': Decoration(
            foreground=Foreground.YELLOW,
            style=Style.RAPID_BLINK
        )
    }
}
