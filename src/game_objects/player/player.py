from value_objects.player.email import Email
from value_objects.player.score import Score
from value_objects.player.credits import Credits
from common.base_entity import BaseEntity
from common.guard import Guard
from uuid import uuid4


class Player(BaseEntity):
    # Constructors
    def __init__(self, **kwargs):
        super().__init__(id=kwargs.get('id', uuid4()))

        self.__username: str = kwargs.get('username', 'Unknown')
        self.__score: Score = kwargs.get('score', Score())
        self.__credits: Credits = kwargs.get('credits', Credits())
        self.__email: Email = kwargs.get('email', Email())

    # Getters
    @property
    def username(self) -> str:
        return self.__username

    @property
    def score(self) -> Score:
        return self.__score

    @property
    def credits(self) -> Credits:
        return self.__credits

    @property
    def email(self) -> Email:
        return self.__email

    ################
    # Update Score #
    ################

    def incrementScore(self, value: int = 1) -> None:
        """
        This method increases score of the player
        """
        Guard.againstZeroOrLess(value, 'value')
        self.__score = Score.create(self.score.value + value)
        self.update()

    def decrementScore(self, value: int = 1) -> None:
        """
        This method decreases score of the player
        """
        Guard.againstZeroOrLess(value, 'value')
        Guard.againstNegative(self.score.value - value, 'score')
        self.__score = Score.create(self.score.value - value)
        self.update()

    ##################
    # Update Credits #
    ##################

    def incrementCredits(self, value: int = 1) -> None:
        """
        This method increases credits of the player
        """
        Guard.againstZeroOrLess(value, 'value')
        self.__credits = Credits.create(self.credits.value + value)
        self.update()

    def decrementCredits(self, value: int = 1) -> None:
        """
        This method decreases credits of the player
        """
        Guard.againstZeroOrLess(value, 'value')
        Guard.againstNegative(self.credits.value - value, 'credits')
        self.__credits = Credits.create(self.credits.value - value)
        self.update()

    def displayInfo(self) -> None:
        """
        This method display's complete information of a player - Can be used for debugging
        """
        print(f"""{'*' * 10} {self} {'*' * 10}
Id:         {self.id}
Name:       {self.username}
Score:      {self.score.__repr__()}
Credits:    {self.credits.__repr__()}
Created:    {self.created_at}
Updated:    {self.updated_at}""")
