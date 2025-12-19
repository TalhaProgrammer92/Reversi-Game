from core.objects.player import Player
from core.misc.func import generate_guid

if __name__ == '__main__':
    player: Player = Player(
        id=generate_guid(),
        name='Talha Ahmad',
        email='talha@gmail.com',
        score=0,
        credits=500,
        xp=100
    )

    print(player)
