from core.objects.base_object import BaseObject
from core.shield.guard import Guard
from uuid import UUID


class Player(BaseObject):
    # Constructor
    def __init__(self, id: UUID, name: str, email: str, score: int, credits: int, xp: int):
        super().__init__(id)

        Guard.againstEmptyOrWhitespace(name, 'name')
        self.__name: str = name

        Guard.againstWrongEmail(email)
        self.__email: str = email

        Guard.againstNegative(score, 'score')
        self.__score: int = score

        Guard.againstNegative(credits, 'credits')
        self.__credits: int = credits

        Guard.againstNegative(xp, 'xp')
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
        Guard.againstEmptyOrWhitespace(value, 'name')
        self.__name = value

    @email.setter
    def email(self, value: str):
        Guard.againstWrongEmail(value)
        self.__email = value

    @score.setter
    def score(self, value: int):
        Guard.againstNegative(value, 'score')
        self.__score = value

    @credits.setter
    def credits(self, value: int):
        Guard.againstNegative(value, 'credits')
        self.__credits = value

    @xp.setter
    def xp(self, value: int):
        Guard.againstNegative(value, 'xp')
        self.__xp = value

    def __repr__(self) -> str:
        """ This method provides object as string for output """
        return f""" {'*' * 10} {self.id} {'*' * 10}
Name:       {self.name}
Email:      {self.email}
Score:      {self.score}
Credits:    {self.credits}
XP:         {self.xp}"""
