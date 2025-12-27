from core.objects.coin import Coin
from core.enums.coin_state import CoinState
from core.shield.guard import Guard


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
    def is_empty(self) -> bool:
        """Check if the cell has no coin"""
        return self.__coin is None

    @property
    def is_occupied(self) -> bool:
        """Check if the cell has a coin"""
        return self.__coin is not None

    @property
    def state(self) -> CoinState | None:
        """Returns the coin state (BLACK/WHITE) or None if empty"""
        return self.__coin.state if self.__coin else None

    ###########
    # Methods #
    ###########

    def place(self, coin: Coin) -> None:
        """Place a coin in this cell"""
        Guard.against_none(coin, 'coin')

        if self.is_occupied:
            raise Exception("Cell is already occupied.")

        self.__coin = coin

    def flip(self) -> None:
        """Flip the coin in this cell (changes BLACK to WHITE or vice versa)"""
        if self.__coin:
            self.__coin.flip()

    def clear(self) -> Coin | None:
        """Remove and return the coin from this cell"""
        coin = self.__coin
        self.__coin = None
        return coin

    def __repr__(self) -> str:
        """String representation of the cell"""
        if self.is_empty:
            return "."  # Empty cell
        return "B" if self.state == CoinState.BLACK else "W"
