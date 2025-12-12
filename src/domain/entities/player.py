from dataclasses import dataclass
from domain.value_objects.player.name import Name
from domain.value_objects.player.score import Score
from domain.value_objects.player.credits import Credits
from uuid import UUID


@dataclass
class Player:
    name : Name
    score : Score
    credits : Credits
    id: UUID
 