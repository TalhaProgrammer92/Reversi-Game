from enum import Enum
from game_objects.base_entity import BaseAttribute


class PlayerAttribute(BaseAttribute, Enum):
    USERNAME = 'username'
    EMAIL = 'email'
    SCORE = 'score'
    CREDITS = 'credits'