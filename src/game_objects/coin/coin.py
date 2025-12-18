from game_objects.base_entity import *
from enums.coin.coin_state import CoinState
from enums.coin.coin_attribute import CoinAttribute
from enums.data_handler.data_type import DataType


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

    @property
    def primary_key(self) -> CoinAttribute:
        return CoinAttribute.ID

    ##########################
    # Attributes & DataTypes #
    ##########################

    @staticmethod
    def getAttributes() -> list[CoinAttribute]:
        """
        This method returns a list of attributes
        """
        return [
            CoinAttribute.ID,
            CoinAttribute.COIN_STATE,
            CoinAttribute.CREATED_AT,
            CoinAttribute.UPDATED_AT
        ]

    @property
    def values_dict(self) -> dict:
        """
        This method returns a dictionary of values
        """
        return {
            CoinAttribute.ID: f'{self.id}',
            CoinAttribute.COIN_STATE: f'{self.state.value}',
            CoinAttribute.CREATED_AT: f'"{self.created_at}"',
            CoinAttribute.UPDATED_AT: f'"{self.updated_at}"'
        }

    @staticmethod
    def getDatatypesWithAttributes() -> dict[CoinAttribute, DataType]:
        """
        This method returns a dictionary with the key-value pairs of attribute name and its datatype
        """
        return {
            CoinAttribute.ID: DataType.INTEGER,
            CoinAttribute.COIN_STATE: DataType.NUMERIC,
            CoinAttribute.CREATED_AT: DataType.TEXT,
            CoinAttribute.UPDATED_AT: DataType.TEXT
        }

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
