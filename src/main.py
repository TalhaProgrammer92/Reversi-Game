from core.misc.position_offset import PositionOffset
from core.enums.coin_state import CoinState
from prototype.text.message import Message
from core.misc.func import generate_guid
from core.misc.position import Position
from core.objects.board import Board
from core.objects.coin import Coin

if __name__ == '__main__':
    board: Board = Board()
    board.initialize()
    board.place_coin(Position(2, 2), Coin(generate_guid, CoinState.WHITE))
    print(board, end='\n\n')

    try:
        position: Position = Position(2, 4)
        offset: PositionOffset = PositionOffset(-1, 2)
        print(f"{position} + {offset} = {position + offset}")
        print(f"{position} - {offset} = {position - offset}")
    except ValueError as e:
        Message.error(f"{e}")
