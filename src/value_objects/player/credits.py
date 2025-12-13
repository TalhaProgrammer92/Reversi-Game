from value_objects.player.score import Score


class Credits(Score):
    def __init__(self, value: int = 0):
        super().__init__(value)
