from dataclasses import dataclass
from dtos.base_dtos.base_dto import BaseDTO


@dataclass(slots=True)
class PlayerDTO(BaseDTO):
    username: str
    email: str
    score: int
    credits: int
