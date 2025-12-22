from prototype.settings import menu_settings
from prototype.text.menu.menu import Menu
from core.shield.guard import Guard
from core.misc.range import Range
from typing import override
from enum import Enum


class MainMenuOption(Enum):
    START_GAME = 1
    LOAD_GAME = 2
    SETTINGS = 3
    CREDITS = 4
    EXIT = 5


class MainMenu(Menu):
    def __init__(self):
        super().__init__(
            title=menu_settings['title']['main-menu'],
            title_decorator=menu_settings['title-decorator']['main-menu'],
            options_decoration=menu_settings['options-decoration']['main-menu']
        )

        # Adding options
        self.add_option('Start Game')
        self.add_option('Load Game')
        self.add_option('Settings')
        self.add_option('Credits')
        self.add_option('Exit')

    @staticmethod
    def options() -> list[MainMenuOption]:
        return [
            MainMenuOption.START_GAME,
            MainMenuOption.LOAD_GAME,
            MainMenuOption.SETTINGS,
            MainMenuOption.CREDITS,
            MainMenuOption.EXIT
        ]

    def get_option(self, value: int) -> MainMenuOption:
        """ This method gets option on the basis of the value """
        Guard.against_out_of_range(Range(1, len(self._options)), value, 'options index')
        return self.options()[value - 1]

    @override
    def display_and_take_input(self) -> MainMenuOption:
        """ This method display's menu and takes input """
        self.display()
        print()
        choice: int = super().take_input()
        return self.get_option(choice)

    @override
    def take_input(self) -> MainMenuOption:
        """ This method read's user input for option selection in the menu """
        choice: int = super().take_input()
        return self.get_option(choice)
