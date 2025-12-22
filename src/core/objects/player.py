from core.enums.attributes.player import PlayerAttribute
from core.objects.base_object import BaseObject
from core.shield.guard import Guard
from uuid import UUID


class Player(BaseObject):
    # Constructor
    def __init__(self, id: UUID, name: str, email: str, score: int, credits: int, xp: int):
        super().__init__(id)

        Guard.against_empty_or_whitespace(name, 'name')
        self.__name: str = name

        Guard.against_wrong_email(email)
        self.__email: str = email

        Guard.against_negative(score, 'score')
        self.__score: int = score

        Guard.against_negative(credits, 'credits')
        self.__credits: int = credits

        Guard.against_negative(xp, 'xp')
        self.__xp: int = xp

    ###########
    # Getters #
    ###########

    @property
    def name(self) -> str:
        return self.__name

    @property
    def email(self) -> str:
        return self.__email

    @property
    def score(self) -> int:
        return self.__score

    @property
    def credits(self) -> int:
        return self.__credits

    @property
    def xp(self) -> int:
        return self.__xp

    ###########
    # Setters #
    ###########

    @name.setter
    def name(self, value: str):
        Guard.against_empty_or_whitespace(value, 'name')
        self.__name = value

    @email.setter
    def email(self, value: str):
        Guard.against_wrong_email(value)
        self.__email = value

    @score.setter
    def score(self, value: int):
        Guard.against_negative(value, 'score')
        self.__score = value

    @credits.setter
    def credits(self, value: int):
        Guard.against_negative(value, 'credits')
        self.__credits = value

    def increment_xp(self, value: int = 1):
        """ This method increases XP by a value """
        Guard.against_zero_or_less(value, 'value')
        self.__xp = value

    @staticmethod
    def get_attributes_list() -> list[PlayerAttribute]:
        """ This method returns attributes list of the player """
        return [
            PlayerAttribute.ID,
            PlayerAttribute.NAME,
            PlayerAttribute.EMAIL,
            PlayerAttribute.SCORE,
            PlayerAttribute.CREDITS,
            PlayerAttribute.XP
        ]

    def __repr__(self) -> str:
        """ This method provides object as string for output """
        return f"""{'*' * 10} {self.id} {'*' * 10}
Name:       {self.name}
Email:      {self.email}
Score:      {self.score}
Credits:    {self.credits}
XP:         {self.xp}"""
