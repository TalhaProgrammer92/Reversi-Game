from prototype.ansi.enums.foreground import Foreground
from prototype.settings import message_settings
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
            text=message_settings['text']['info'],
            decoration=message_settings['decoration']['info']
        )

        print(Message(header, message))

    @staticmethod
    def error(message: str) -> None:
        header: Text = Text(
            text=message_settings['text']['error'],
            decoration=message_settings['decoration']['error']
        )

        print(Message(header, message))

    @staticmethod
    def warning(message: str) -> None:
        header: Text = Text(
            text=message_settings['text']['warning'],
            decoration=message_settings['decoration']['warning']
        )

        print(Message(header, message))

    @staticmethod
    def success(message: str) -> None:
        header: Text = Text(
            text=message_settings['text']['success'],
            decoration=message_settings['decoration']['success']
        )

        print(header, message)

    def __repr__(self) -> str:
        return self.header.__repr__() + ' ' + self.message
