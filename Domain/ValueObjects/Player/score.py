class Score:
    # Constructor
    def __init__(self, score: int = 0):
        self.__score: int = score

    # Getter
    @property
    def value(self) -> int:
        return self.__score

    # Method - Increment score by a number
    def increment(self, value: int = 1) -> 'Score':
        return Score(self.value + value)

    # Method - Reset the score
    def reset(self) -> None:
        self.__score = 0

    # Method - Representation
    def __repr__(self) -> str:
        return str(self.value)
