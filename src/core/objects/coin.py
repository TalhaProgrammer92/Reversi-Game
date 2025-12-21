from core.enums.attributes.coin import CoinAttribute
from core.objects.base_object import BaseObject
from core.enums.coin_state import CoinState
from core.misc.position import Position
from uuid import UUID


class Coin(BaseObject):
    # Constructor
    def __init__(self, id: UUID, state: CoinState = CoinState.WHITE, position: Position | None = None):
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

    @property
    def placed(self) -> bool:
        return self.position is not None

    def place(self, position: Position) -> None:
        """ This method places the coin on board """
        # Check if coin is already placed
        if self.placed:
            raise Exception(f"Coin is already placed at position {self.position}.")

        self.__position = position

    def flip(self) -> None:
        """ This method switches the state of the coin """
        self.__state = CoinState.WHITE if self.__state == CoinState.BLACK else CoinState.BLACK

    @staticmethod
    def get_attributes_list() -> list[CoinAttribute]:
        """ This method returns attributes list of the coin """
        return [
            CoinAttribute.ID,
            CoinAttribute.STATE,
            CoinAttribute.POSITION_ROW,
            CoinAttribute.POSITION_COLUMN,
            CoinAttribute.IS_PLACED
        ]

    def __repr__(self) -> str:
        """ This method provides object as string for output """
        return f"""{'*' * 10} {self.id} {'*' * 10}
State:      {self.state.name}
Position:   {self.position}"""
