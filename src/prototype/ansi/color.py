from prototype.ansi.enums.foreground import Foreground
from prototype.ansi.enums.background import Background
from prototype.ansi.enums.style import Style

RESET = '\033[0m'


class Decoration:
    def __init__(self, **kwargs):
        self.fg: Foreground | None = kwargs.get('foreground', None)
        self.bg: Background | None = kwargs.get('background', None)
        self.style: Style | None = kwargs.get('style', None)

    ###########
    # Getters #
    ###########

    @property
    def exists(self) -> bool:
        return self.fg is not None or self.bg is not None or self.style is not None

    @property
    def code(self) -> str:
        # If the decoration doesn't exist
        if not self.exists:
            return ''

        ansi_code: str = '\033['

        # Add foreground code
        if self.fg:
            ansi_code += self.fg.value

        # Add background code
        if self.bg:
            if self.fg:
                ansi_code += ';'

            ansi_code += self.bg.value

        # Add style code
        if self.style:
            if self.bg or self.fg:
                ansi_code += ';'

            ansi_code += self.style.value

        return ansi_code + 'm'

def colored_text(**kwargs) -> str:
    """ This function provides ansi encoded text """
    text: str = kwargs.get('text', 'Text')
    decor: Decoration | None = kwargs.get('decoration', Decoration())

    return decor.code + text + RESET
