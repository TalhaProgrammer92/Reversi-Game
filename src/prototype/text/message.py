from prototype.ansi.enums.foreground import Foreground
from prototype.ansi.enums.style import Style
from prototype.ansi.color import Decoration
from prototype.text.text import Text


class Message:
    def __init__(self, header: Text, message: str):
        self.header: Text = header
        self.message: str = message

    @staticmethod
    def info(message: str) -> None:
        header: Text = Text(
            text='[INFO]',
            decoration=Decoration(
                foreground=Foreground.BRIGHT_CYAN,
                style=Style.BOLD
            )
        )

        print(Message(header, message))

    @staticmethod
    def error(message: str) -> None:
        header: Text = Text(
            text='[ERROR]',
            decoration=Decoration(
                foreground=Foreground.BRIGHT_RED,
                style=Style.BOLD
            )
        )

        print(Message(header, message))

    @staticmethod
    def warning(message: str) -> None:
        header: Text = Text(
            text='[WARNING]',
            decoration=Decoration(
                foreground=Foreground.BRIGHT_YELLOW,
                style=Style.BOLD
            )
        )

        print(Message(header, message))

    @staticmethod
    def success(message: str) -> None:
        header: Text = Text(
            text='[SUCCESS]',
            decoration=Decoration(
                foreground=Foreground.BRIGHT_GREEN,
                style=Style.BOLD
            )
        )

        print(header, message)

    def __repr__(self) -> str:
        return self.header.__repr__() + ' ' + self.message
