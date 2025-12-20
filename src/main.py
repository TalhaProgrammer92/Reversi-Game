from core.objects.player import Player
from core.objects.coin import Coin
from core.misc.func import *
from core.misc.position import Position

if __name__ == '__main__':
    player: Player = Player(
        id=generate_guid(),
        name='Talha Ahmad',
        email='talha@gmail.com',
        score=0,
        credits=500,
        xp=100
    )

    # print(player)

    coin: Coin = Coin(
        generate_guid()
    )
    coin.place(Position(2, 5))

    # print(coin)

    lp: str = to_label_position(Position(1, 4))
    pos: Position = from_label_position(lp)
    print(lp, pos)
