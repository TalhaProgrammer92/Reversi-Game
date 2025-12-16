from datetime import datetime as dt
from data.handlers.common import DataType


class BaseAttribute:
    ID = 'id'
    CREATED_AT = 'created_at'
    UPDATED_AT = 'updated_at'


class BaseEntity:
    # Constructor
    def __init__(self, **kwargs):
        self._id: int = kwargs.get('id', 0)
        self._created_at: dt = kwargs.get('created_at', dt.now())
        self._updated_at: dt = kwargs.get('updated_at', dt.now())

    @staticmethod
    def getAttributesDict() -> dict:
        return {
            BaseAttribute.ID: BaseAttribute.ID,
            BaseAttribute.CREATED_AT: BaseAttribute.CREATED_AT,
            BaseAttribute.UPDATED_AT: BaseAttribute.UPDATED_AT
        }

    @staticmethod
    def getDatatypesWithAttributes() -> dict:
        return {
            BaseAttribute.ID: DataType.INTEGER,
            BaseAttribute.CREATED_AT: DataType.TEXT,
            BaseAttribute.UPDATED_AT: DataType.TEXT
        }

    ###########
    # Getters #
    ###########

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


if __name__ == '__main__':
    base: BaseEntity = BaseEntity(id=2)
    print(base.id, base.created_at, base.updated_at, sep=' --- ')
    print(BaseAttribute.ID, BaseAttribute.CREATED_AT, BaseAttribute.UPDATED_AT)
