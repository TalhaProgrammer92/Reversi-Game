from core.objects.base_object import BaseObject
from core.enums.coin_state import CoinState
from core.misc.position import Position
from uuid import UUID


class Coin(BaseObject):
    # Constructor
    def __init__(self, id: UUID, state: CoinState, position: Position | None = None):
        super().__init__(id)
        self.__state: CoinState = state
        self.__position: Position | None = position

    ###########
    # Getters #
    ###########

    @property
    def state(self) -> CoinState:
        return self.__state

    @property
    def position(self) -> Position | None:
        return self.__position

    def place(self, position: Position) -> None:
        """ This method places the coin on board """
        # Check if coin is already placed
        if self.is_placed():
            raise Exception(f"Coin is already placed at position {self.position}.")

        self.__position = position

    def switch(self) -> None:
        """ This method switches the state of the coin """
        self.__state = CoinState.WHITE if self.__state == CoinState.BLACK else CoinState.BLACK

    # Check if the coin is placed or not
    is_placed: bool = lambda self: self.__position is None
