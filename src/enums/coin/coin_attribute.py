from enum import Enum
from game_objects.base_entity import BaseAttribute


class CoinAttribute(BaseAttribute, Enum):
    COIN_STATE = 'state'
