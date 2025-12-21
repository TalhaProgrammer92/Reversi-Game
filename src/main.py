from prototype.text.menu.main_menu import *
from prototype.text.message import Message
from core.misc.func import clear_screen

if __name__ == '__main__':
    menu: MainMenu = MainMenu()
    option: int = 0

    while True:
        clear_screen()
        menu.display()
        print()
        Message.info(f"You've selected '{menu.get_option(option).name if option > 0 else 'None'}'")
        option = menu.take_input()

        if option == MainMenuOption.EXIT.value:
            clear_screen()
            print('Quiting...')
            break
