from common.guard import Guard


class Score:
    def __init__(self, value: int = 0):
        # Attribute
        self.__score: int

        # Guard against invalid score
        Guard.againstNegative(value, 'score')

        # Assign value
        self.__score = value

    @property
    def value(self) -> int:
        return self.__score

    @staticmethod
    def create(value: int = 0) -> Score:
        """
        This method creates a new object
        """
        return Score(value)

    def __repr__(self) -> str:
        """
        This method returns object as string for output
        """
        return str(self.__score)
