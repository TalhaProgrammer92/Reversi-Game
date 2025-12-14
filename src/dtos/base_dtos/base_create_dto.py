from dtos.base_dtos.base_dto import BaseDTO
from dataclasses import dataclass
from datetime import datetime
from uuid import uuid4


@dataclass(slots=True)
class BaseCreateDTO(BaseDTO):
    id = uuid4()
    created_at = datetime.now()
    updated_at = datetime.now()
