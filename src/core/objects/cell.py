from core.enums.cell_state import CellState
from core.misc.position import Position
from core.shield.guard import Guard
from core.objects.coin import Coin


class Cell:
    """
    Represents a single cell on the Reversi board.
    A cell can either be empty or contain a coin.
    """

    # Constructor
    def __init__(self):
        self.__coin: Coin | None = None

    ###########
    # Getters #
    ###########

    @property
    def coin(self) -> Coin | None:
        """Returns the coin in this cell, or None if empty"""
        return self.__coin

    @property
    def state(self) -> CellState:
        """Returns the cell state (Empty / Occupied) """
        return CellState.OCCUPIED if self.__coin else CellState.EMPTY

    ###########
    # Methods #
    ###########

    def place(self, coin: Coin) -> None:
        """Place a coin in this cell"""
        Guard.against_none(coin, 'coin')

        if self.state == CellState.OCCUPIED:
            raise Exception("Cell is already occupied.")

        self.__coin = coin

    def flip(self) -> None:
        """Flip the coin in this cell"""
        if self.state == CellState.EMPTY:
            raise Exception("Cell is empty")

        self.__coin.flip()

    def clear(self) -> Coin | None:
        """Remove and return the coin from this cell"""
        coin = self.__coin
        self.__coin = None
        return coin

    def __repr__(self) -> str:
        """String representation of the cell"""
        return '.' if self.state == CellState.EMPTY else self.coin.state.name[0]
