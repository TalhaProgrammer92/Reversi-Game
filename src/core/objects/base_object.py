from uuid import UUID


class BaseObject:
    def __init__(self, id: UUID):
        self._id: UUID = id

    @property
    def id(self) -> UUID:
        return self._id
