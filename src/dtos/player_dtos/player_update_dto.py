from dataclasses import dataclass
from typing import Optional
from dtos.base_dtos.base_update_dto import BaseUpdateDTO


@dataclass(slots=True)
class UpdatePlayerDTO(BaseUpdateDTO):
    username: Optional[str] = None
    email: Optional[str] = None
