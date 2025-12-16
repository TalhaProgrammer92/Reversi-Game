from value_objects.player.email import Email
from value_objects.player.score import Score
from value_objects.player.credits import Credits
from game_objects.base_entity import *
from shield.guard import Guard
from data.handlers.common import DataType
from enum import Enum


class PlayerAttribute(BaseAttribute, Enum):
    USERNAME = 'username'
    EMAIL = 'email'
    SCORE = 'score'
    CREDITS = 'credits'


class Player(BaseEntity):
    # Constructors
    def __init__(self, **kwargs):
        super().__init__(id=kwargs.get('id', 0))

        self.__username: str = kwargs.get('username', 'Unknown')
        self.__score: Score = kwargs.get('score', Score())
        self.__credits: Credits = kwargs.get('credits', Credits())
        self.__email: Email = kwargs.get('email', Email())

    ###########
    # Getters #
    ###########

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

    @staticmethod
    def getAttributesDict() -> dict:
        return {
            PlayerAttribute.ID: PlayerAttribute.ID,
            PlayerAttribute.USERNAME: PlayerAttribute.USERNAME.value,
            PlayerAttribute.EMAIL: PlayerAttribute.EMAIL.value,
            PlayerAttribute.SCORE: PlayerAttribute.SCORE.value,
            PlayerAttribute.CREDITS: PlayerAttribute.CREDITS.value,
            PlayerAttribute.CREATED_AT: PlayerAttribute.CREATED_AT,
            PlayerAttribute.UPDATED_AT: PlayerAttribute.UPDATED_AT
        }

    @property
    def values_dict(self) -> dict:
        return {
            PlayerAttribute.ID: f'{self.id}',
            PlayerAttribute.USERNAME: f'"{self.username}"',
            PlayerAttribute.EMAIL: f'"{self.email.value}"',
            PlayerAttribute.SCORE: f'{self.score.value}',
            PlayerAttribute.CREDITS: f'{self.credits.value}',
            PlayerAttribute.CREATED_AT: f'"{self.created_at}"',
            PlayerAttribute.UPDATED_AT: f'"{self.updated_at}"'
        }

    @staticmethod
    def getDatatypesWithAttributes() -> dict:
        """
        This method returns a dictionary with the key-value pairs of attribute name and its datatype
        """
        base: dict = BaseEntity.getDatatypesWithAttributes()
        player: dict = {
            PlayerAttribute.USERNAME.value: DataType.TEXT,
            PlayerAttribute.EMAIL.value: DataType.TEXT,
            PlayerAttribute.SCORE.value: DataType.INTEGER,
            PlayerAttribute.CREDITS.value: DataType.INTEGER
        }
        return base | player

    ################
    # Update Score #
    ################

    def incrementScore(self, value: int = 1) -> None:
        """
        This method increases score of the player
        """
        Guard.againstZeroOrLess(value, 'score')
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

    ########
    # Misc #
    ########

    @staticmethod
    def table_name() -> str:
        """
        This method returns table name for the player entity
        """
        return 'Players'

    def displayInfo(self) -> None:
        """
        This method display's complete information of a player - Can be used for debugging
        """
        print(f"""{'*' * 10} {self} {'*' * 10}
Id:         {self.id}
Name:       {self.username}
Email:      {self.email.value}
Score:      {self.score.value}
Credits:    {self.credits.value}
Created:    {self.created_at}
Updated:    {self.updated_at}""")

if __name__ == '__main__':
    player: Player = Player(
        id=1,
        username='Talha Ahmad',
        email=Email('talha@gmail.com'),
        score=Score(24),
        credits=Credits(1500)
    )
    # player.displayInfo()
    print(
        ' --- '.join(player.getAttributesDict().values()),
        ' --- '.join(player.values_dict.values()),
        sep='\n'
    )

    print(player.values_dict[PlayerAttribute.EMAIL], player.email.value, sep=' <> ')
    # print(player.getAttributesDict().__doc__)
