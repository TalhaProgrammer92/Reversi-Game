from prototype.ansi.enums.style import Style
from prototype.ansi.color import Decoration
from prototype.text.text import Text
from core.shield.guard import Guard
from core.misc.func import print_n


class Menu:
    def __init__(self, title: Text, title_decorator: str, options_decoration: Decoration):
        self._title: Text = title

        Guard.againstSize(1, title_decorator, 'decorator')
        Guard.againstWhitespace(title_decorator, 'decorator')
        self._title_decorator: str = title_decorator
        self._max_length: int = len(self.title.value)

        self._options_decoration: Decoration = options_decoration
        self._options: list[Text] = []

    ###########
    # Getters #
    ###########

    @property
    def title(self) -> Text:
        return self._title

    @property
    def title_decorator(self) -> Text:
        return Text(
            text=self._title_decorator,
            decoration=self.title.decoration
        )

    def addOption(self, option: str) -> None:
        """ This method is used to add an option to the menu """
        # Add an option to the list
        Guard.againstEmptyOrWhitespace(option, 'option')

        self._options.append(Text(text=option, decoration=self._options_decoration))

        # Update max length
        if self._max_length < len(option):
            self._max_length = len(option)

    def _print_title(self) -> None:
        """ This method prints title of the menu """
        # Calculations
        """
        self._max_length: Maximum text length in title and options
        (
            2: Brackets
            len(str(len(self._options))): Number of digits in total options
            1: White-Space
        )
        2: Symbols
        """
        decor_size: int = self._max_length + 2 + len(str(len(self._options))) + 1 + 2
        remaining_size = decor_size - len(self.title.value) - 2

        padding: int = int(remaining_size / 2)

        # Upper band
        print_n(
            value=self.title_decorator.__repr__(),
            limit=decor_size
        )

        # Left Symbol
        print(self.title_decorator, end='')

        # Left Padding
        print_n(
            value=' ',
            limit=padding + 1 if remaining_size % 2 else padding,
            line_break=False
        )

        # Title
        print(self.title, end='')

        # Right Padding
        print_n(
            value=' ',
            limit=padding,
            line_break=False
        )

        # Right Symbol
        print(self.title_decorator)

        # Lower band
        print_n(
            value=self.title_decorator.__repr__(),
            limit=decor_size
        )

    def _print_options(self) -> None:
        """ This method prints all options """
        for i in range(len(self._options)):
            # Number
            print(Text(
                text=f'[{i + 1}] ',
                decoration=Decoration(
                    foreground=self._options_decoration.fg,
                    background=self._options_decoration.bg,
                    style=Style.BOLD
                )
            ), end='')

            # Option
            print(self._options[i])

    def display(self) -> None:
        """ This method displays the menu on the terminal """
        # Print title
        self._print_title()
        self._print_options()

    def take_input(self):
        """ This method read's user input for option selection in the menu """
        pass
