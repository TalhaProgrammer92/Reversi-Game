from core.misc.position import Position
from core.shield.guard import Guard
from uuid import uuid4

# Generates a random GUID
generate_guid = lambda : uuid4()

def to_label_position(position: Position) -> str:
    """ This function converts a normal position to a labeled position """
    row: str = str(position.row)
    labels: str = "ABCDEFGH"
    column: str = labels[position.column - 1]

    return row + column

def from_label_position(position: str) -> Position:
    """ This function converts a labeled position to a normal position """
    Guard.againstSize(2, position, 'position')

    row: int = int(position[0])
    column: int = ord(position[1].upper()) - ord('A') + 1

    return Position(row, column)

def print_n(value: str, limit: int, line_break: bool = True) -> None:
    """ This function prints a given string in N times """
    Guard.againstZeroOrLess(limit, 'limit')

    for count in range(limit):
        print(value, end='')

    if line_break:
        print()
