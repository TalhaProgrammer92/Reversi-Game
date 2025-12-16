from game_objects.base_entity import *
from enums.coin_state import CoinState
from data.handlers.common import DataType
from enum import Enum


class CoinAttribute(BaseAttribute, Enum):
    COIN_STATE = 'state'


class Coin(BaseEntity):
    def __init__(self, **kwargs):
        super().__init__(id=kwargs.get('id', 0))

        # self.__position: Position = kwargs.get('position', Position())
        self.__coin_state: CoinState = kwargs.get('coin_state', CoinState.BLACK)

    ###########
    # Getters #
    ###########

    @property
    def state(self) -> CoinState:
        return self.__coin_state

    @staticmethod
    def getAttributesDict() -> dict:
        base: dict = BaseEntity.getAttributesDict()
        coin: dict = {
            CoinAttribute.COIN_STATE: CoinAttribute.COIN_STATE.value,
        }
        return base | coin

    @property
    def values_dict(self) -> dict:
        return {
            CoinAttribute.ID: f'{self.id}',
            CoinAttribute.COIN_STATE: f'{self.state.value}',
            CoinAttribute.CREATED_AT: f'"{self.created_at}"',
            CoinAttribute.UPDATED_AT: f'"{self.updated_at}"'
        }

    @staticmethod
    def getDatatypesWithAttributes() -> dict:
        """
        This method returns a dictionary with the key-value pairs of attribute name and its datatype
        """
        base: dict = BaseEntity.getDatatypesWithAttributes()
        coin: dict = {
            CoinAttribute.COIN_STATE.value: DataType.NUMERIC
        }
        return base | coin

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

    ########
    # Misc #
    ########

    @staticmethod
    def table_name() -> str:
        """
        This method returns table name for the coint entity
        """
        return 'Coins'

    def displayInfo(self) -> None:
        """
        This method display's complete information of a coin - Can be used for debugging
        """
        print(f"""{'*' * 10} {self} {'*' * 10}
Id:         {self.id}
State:      {self.state.name}
Created:    {self.created_at}
Updated:    {self.updated_at}""")

if __name__ == '__main__':
    coin: Coin = Coin(id=2, coin_state=CoinState.BLACK)
    print(
        ' --- '.join(coin.getAttributesDict().values()),
        ' --- '.join(coin.values_dict.values()),
        sep='\n'
    )
