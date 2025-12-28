from core.misc.position_offset import PositionOffset
from enum import Enum


class Direction(Enum):
    # Vertical
    TOP = PositionOffset(row=1, column=0)
    BOTTOM = PositionOffset(row=-1, column=0)

    # Horizontal
    LEFT = PositionOffset(row=0, column=-1)
    RIGHT = PositionOffset(row=0, column=1)

    # Diagonal
    TOP_LEFT = PositionOffset(row=1, column=-1)
    TOP_RIGHT = PositionOffset(row=1, column=1)
    BOTTOM_LEFT = PositionOffset(row=-1, column=-1)
    BOTTOM_RIGHT = PositionOffset(row=-1, column=1)
