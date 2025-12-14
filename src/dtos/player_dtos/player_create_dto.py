from dataclasses import dataclass
from dtos.base_dtos.base_create_dto import BaseCreateDTO


@dataclass(slots=True)
class PlayerCreateDTO(BaseCreateDTO):
    username: str
    email: str
