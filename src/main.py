from prototype.text.menu.main_menu import *
from prototype.text.message import Message
from core.misc.func import clear_screen

if __name__ == '__main__':
    menu: MainMenu = MainMenu()
    option: MainMenuOption | None = None

    while True:
        clear_screen()
        Message.info(f"You've selected: '{option.name if option is not None else "None"}'\n")
        option = menu.display_and_take_input()

        if option == MainMenuOption.EXIT:
            clear_screen()
            print('Quiting...')
            break
