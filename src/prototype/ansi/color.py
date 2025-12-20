from prototype.ansi.enums.foreground import Foreground
from prototype.ansi.enums.background import Background
from prototype.ansi.enums.style import Style

RESET = '\033[0m'

def colored_text(**kwargs) -> str:
    text: str = kwargs.get('text', 'Text')
    fg: Foreground | None = kwargs.get('foreground', None)
    bg: Background | None = kwargs.get('background', None)
    style: Style | None = kwargs.get('style', None)

    code: str = '\033['

    if fg:
        code += fg.value
    if bg:
        code += ';' + bg.value
    if style:
        code += ';' + style.value

    code += 'm' + text + RESET

    return code
