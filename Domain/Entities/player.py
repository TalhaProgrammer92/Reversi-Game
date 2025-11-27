from uuid import uuid4
from datetime import datetime as dt
from Domain.Entities.base_entity import BaseEntity
from Domain.ValueObjects.Player.name import Name
from Domain.ValueObjects.Player.score import Score

class Player(BaseEntity):
    # Constructor
    def __init__(self, **kwargs):
        # Base class attributes
        super().__init__(id=kwargs.get('id', uuid4()),
                         created_at=kwargs.get('created_at', dt.now()),
                         updated_at=kwargs.get('updated_at', None))

        self.name: Name = kwargs.get('name', Name(''))
        self.score: Score = kwargs.get('score', Score())

    # Method - Increase score
    def incrementScore(self, value: int = 1) -> None:
        self.score = self.score.increment(value)

    # Method - Representation
    def __repr__(self) -> str:
        return f'''Id:         {self.id}
Name:       {self.name.value}
Score:      {self.score.value}
Created:    {self.created_at}
Updated:    {self.updated_at}'''
