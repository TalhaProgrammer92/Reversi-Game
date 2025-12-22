from core.misc.position import Position
from core.shield.guard import Guard
from os import system, name
from uuid import uuid4

# Generates a random GUID
generate_guid = lambda : uuid4()

def to_label_position(position: Position) -> str:
    """ This function converts a normal position to a labeled position """
    row: str = str(position.row)
    labels: str = "ABCDEFGH"
    column: str = labels[position.column - 1]

    return column + row

def from_label_position(position: str) -> Position:
    """ This function converts a labeled position to a normal position """
    # Validation Checks
    Guard.against_size(2, position, 'position')

    if not position[1].isdigit():
        raise Exception("The position must contain a digit.")
    if not position[0] in 'ABCDEFGH':
        raise Exception("The position must contain a label.")

    # Conversion
    row: int = int(position[1])
    column: int = ord(position[0]) - ord('A') + 1

    return Position(row, column)

def print_n(value: str, limit: int, line_break: bool = True) -> None:
    """ This function prints a given string in N times """
    Guard.against_zero_or_less(limit, 'limit')

    for count in range(limit):
        print(value, end='')

    if line_break:
        print()

def clear_screen() -> None:
    """ This function clears console/terminal screen """
    command: str = 'cls' if name == 'nt' else 'clear'
    system(command)
