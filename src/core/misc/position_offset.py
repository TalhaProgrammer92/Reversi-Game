class PositionOffset:
    def __init__(self, row: int, column: int):
        self.__row: int = row
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

    def __repr__(self) -> str:
        return f'({self.row}, {self.column})'
