from dataclasses import dataclass
from domain.enums.coin_state import CoinState

@dataclass
class Coin:
    state : CoinState
    