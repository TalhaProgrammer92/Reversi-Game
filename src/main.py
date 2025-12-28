from core.enums.coin_state import CoinState
from core.misc.func import generate_guid
from core.misc.position import Position
from core.objects.board import Board
from core.objects.coin import Coin

if __name__ == '__main__':
    board: Board = Board()
    board.initialize()
    board.place_coin(Position(2, 2), Coin(generate_guid, CoinState.WHITE))
    print(board)
