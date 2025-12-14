from dataclasses import dataclass
from uuid import UUID
from datetime import datetime


@dataclass(slots=True)
class BaseDTO:
    id: UUID
    created_at: datetime
    updated_at: datetime
