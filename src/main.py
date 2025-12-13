from game_objects.player.player import Player
from game_objects.coin.coin import Coin

if __name__ == '__main__':
    player: Player = Player(username="Talha Ahmad", score=12, credits=1500)
    coin: Coin = Coin()

    player.displayInfo()
    print()
    coin.displayInfo()
