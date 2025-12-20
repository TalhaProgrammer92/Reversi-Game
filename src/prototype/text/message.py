from prototype.ansi.enums.foreground import Foreground
from prototype.ansi.enums.style import Style
from prototype.ansi.color import Decoration
from prototype.text.text import Text


class Message:
    @staticmethod
    def info(message: str) -> None:
        header: Text = Text(
            text='[INFO]',
            decoration=Decoration(
                foreground=Foreground.BRIGHT_CYAN,
                style=Style.BOLD
            )
        )

        text: Text = Text(
            text=message,
            decoration=Decoration(
                style=Style.ITALIC
            )
        )

        print(header, text, sep=' ')

    @staticmethod
    def error(message: str) -> None:
        header: Text = Text(
            text='[ERROR]',
            decoration=Decoration(
                foreground=Foreground.BRIGHT_RED,
                style=Style.BOLD
            )
        )

        text: Text = Text(
            text=message,
            decoration=Decoration(
                style=Style.ITALIC
            )
        )

        print(header, text, sep=' ')

    @staticmethod
    def warning(message: str) -> None:
        header: Text = Text(
            text='[WARNING]',
            decoration=Decoration(
                foreground=Foreground.BRIGHT_YELLOW,
                style=Style.BOLD
            )
        )

        text: Text = Text(
            text=message,
            decoration=Decoration(
                style=Style.ITALIC
            )
        )

        print(header, text, sep=' ')

    @staticmethod
    def success(message: str) -> None:
        header: Text = Text(
            text='[SUCCESS]',
            decoration=Decoration(
                foreground=Foreground.BRIGHT_GREEN,
                style=Style.BOLD
            )
        )

        text: Text = Text(
            text=message,
            decoration=Decoration(
                style=Style.ITALIC
            )
        )

        print(header, text, sep=' ')
