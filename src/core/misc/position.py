from core.misc.position_offset import PositionOffset
from core.shield.guard import Guard
from core.misc.range import Range


class Position:
    # Constructor
    def __init__(self, row: int, column: int):
        Guard.against_out_of_range(Position.range(), row, 'row')
        self._row: int = row

        Guard.against_out_of_range(Position.range(), column, 'column')
        self._column: int = column

    ###########
    # Getters #
    ###########

    @property
    def row(self) -> int:
        return self._row

    @property
    def column(self) -> int:
        return self._column

    @staticmethod
    def range() -> Range:
        return Range(1, 8)

    ################
    # Calculations #
    ################

    def __add__(self, other: 'Position' | PositionOffset) -> 'Position':
        position: Position = Position(row=self.row + other.row, column=self.column + other.column)
        Guard.against_out_of_range(Position.range(), self.row, 'row')
        Guard.against_out_of_range(Position.range(), self.column, 'column')

        return position

    def __sub__(self, other: 'Position' | PositionOffset) -> 'Position':
        position: Position = Position(row=self.row - other.row, column=self.column - other.column)
        Guard.against_out_of_range(Position.range(), self.row, 'row')
        Guard.against_out_of_range(Position.range(), self.column, 'column')

        return position

    def __repr__(self) -> str:
        """ This method provides object as string for output """
        return f"({self.row}, {self.column})"
