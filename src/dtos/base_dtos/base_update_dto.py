from datetime import datetime
from dataclasses import dataclass
from dtos.base_dtos.base_dto import BaseDTO


@dataclass(slots=True)
class BaseUpdateDTO(BaseDTO):
    updated_at = datetime.now()
