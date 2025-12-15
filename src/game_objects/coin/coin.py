from common.base_entity import BaseEntity
from enums.coin_state import CoinState


class Coin(BaseEntity):
    def __init__(self, **kwargs):
        super().__init__(id=kwargs.get('id', 0))

        self.__coin_state: CoinState = kwargs.get('coin_state', CoinState.BLACK)

    # Getter
    @property
    def state(self) -> CoinState:
        return self.__coin_state

    ######################
    # Update Coin States #
    ######################

    def switchStateToWhite(self) -> None:
        """
        This method switches the coin state to 'white'
        """
        self.__coin_state = CoinState.WHITE
        self.update()

    def switchStateToBlack(self) -> None:
        """
        This method switches the coin state to 'black'
        """
        self.__coin_state = CoinState.BLACK
        self.update()

    def displayInfo(self) -> None:
        """
        This method display's complete information of a coin - Can be used for debugging
        """
        print(f"""{'*' * 10} {self} {'*' * 10}
Id:         {self.id}
State:      {self.state.name}
Created:    {self.created_at}
Updated:    {self.updated_at}""")
