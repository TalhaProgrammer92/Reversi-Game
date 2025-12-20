from prototype.ansi.color import Decoration, colored_text
from core.shield.guard import Guard


class Text:
    def __init__(self, text: str, decoration: Decoration = Decoration()):
        Guard.againstEmptyOrWhitespace(text, 'text')
        self.__text: str = text
        self.__decoration: Decoration = decoration

    ###########
    # Getters #
    ###########

    @property
    def value(self) -> str:
        return self.__text

    @property
    def decoration(self) -> Decoration:
        return self.__decoration

    def __repr__(self) -> str:
        return colored_text(text=self.value, decoration=self.decoration)
