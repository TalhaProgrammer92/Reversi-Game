from prototype.ansi.color import Decoration, colored_text
from core.shield.guard import Guard


class Text:
    def __init__(self, text: str, decoration: Decoration = Decoration()):
        Guard.againstEmpty(text, 'text')
        self.__text: str = text
        self.__decoration: Decoration = decoration

    def __repr__(self) -> str:
        return colored_text(text=self.__text, decoration=self.__decoration)
