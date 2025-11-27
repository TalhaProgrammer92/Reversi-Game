from Domain.Entities.player import Player
from Domain.ValueObjects.Player.name import Name

def main():
    player: Player = Player(name=Name("Talha Ahmad"))
    player.incrementScore(3)

    print(player)


if __name__ == '__main__':
    main()
