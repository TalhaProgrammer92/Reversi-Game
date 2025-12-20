from core.shield.guard import Guard
from core.misc.range import Range


class Position:
    # Constructor
    def __init__(self, row: int, column: int):
        Guard.againstOutOfRange(Position.range(), row, 'row')
        self.__row: int = row

        Guard.againstOutOfRange(Position.range(), column, 'column')
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

    @staticmethod
    def range() -> Range:
        return Range(1, 8)

    def __repr__(self) -> str:
        """ This method provides object as string for output """
        return f"({self.row}, {self.column})"
