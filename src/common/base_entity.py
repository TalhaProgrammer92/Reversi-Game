from datetime import datetime as dt


class BaseEntity:
    # Constructor
    def __init__(self, **kwargs):
        self._id: int = kwargs.get('id', 0)
        self._created_at: dt = kwargs.get('created_at', dt.now())
        self._updated_at: dt = kwargs.get('updated_at', dt.now())

    # Getters
    @property
    def id(self) -> int:
        return self._id

    @property
    def created_at(self) -> dt:
        return self._created_at

    @property
    def updated_at(self) -> dt:
        return self._updated_at

    def update(self) -> None:
        """
        This method updates 'updated_at' time for an entity
        """
        self._updated_at = dt.now()
