from dataclasses import dataclass
from typing import Optional
from dtos.base_dtos.base_paged_filter_dto import BasePagedFilterDTO


@dataclass(slots=True)
class PlayerFilterDTO(BasePagedFilterDTO):
    username_contains: Optional[str] = None
    email: Optional[str] = None
    min_score: Optional[int] = None
    max_score: Optional[int] = None
    min_credits: Optional[int] = None
    max_credits: Optional[int] = None
