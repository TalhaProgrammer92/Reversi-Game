from core.misc.position import Position


class Size(Position):
    def __init__(self, rows: int, columns: int):
        super().__init__(rows, columns)
