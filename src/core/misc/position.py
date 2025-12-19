from sys import orig_argv

from core.shield.guard import Guard
from core.misc.range import Range


class Position:
    # Constructor
    def __init__(self, row: int, column: int):
        Guard.againstOutOfRange(self.range, row, 'row')
        self.__row: int = row

        Guard.againstOutOfRange(self.range, column, 'column')
        self.__column: int = column

    ###########
    # Getters #
    ###########

    @property
    def row(self) -> int:
        return self.__row

    @property
    def column(self) -> int:
        return self.__column

    @property
    def range(self) -> Range:
        range: Range = Range(1, 8)
        return range

    def __repr__(self) -> str:
        """ This method provides object as string for output """
        return f"({self.row}, {self.column})"
