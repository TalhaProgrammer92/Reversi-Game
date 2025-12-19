from game_objects.player.player import Player
from game_objects.coin.coin import Coin
from enums.data_handler.data_type import DataType
from data.handlers.common.foreign_key_constraint import ForeignKeyConstraint
from shield.guard import Guard


class TableItem:
    def __init__(self, **kwargs):
        self.__name: str = kwargs.get('name', 'title')
        self.__data_type: DataType = kwargs.get('type', DataType.NULL)
        self.__is_primary_key: bool = kwargs.get('is_primary_key', False)
        self.__foreign_key_constraint: ForeignKeyConstraint | None = kwargs.get('foreign_key', None)
        self.__nullable: bool = kwargs.get('nullable', True) if not self.is_primary_or_foreign_key else False

    ###########
    # Getters #
    ###########
    @property
    def name(self) -> str:
        return self.__name

    @property
    def data_type(self) -> DataType:
        return self.__data_type

    @property
    def is_primary_key(self) -> bool:
        return self.__is_primary_key

    @property
    def foreign_key_constraint(self) -> ForeignKeyConstraint | None:
        return self.__foreign_key_constraint

    @property
    def is_primary_or_foreign_key(self) -> bool:
        return self.__is_primary_key or self.__foreign_key_constraint is not None

    def generateHeader(self) -> str:
        header: str = f"{self.name} {self.data_type.value}"

        # Add nullable constraint
        if not self.__nullable and not self.is_primary_or_foreign_key:
            header += ' NOT NULL'

        # Add primary key constraint
        if self.is_primary_key:
            header += ' PRIMARY KEY AUTOINCREMENT'

        # Add foreign key constraint
        if self.foreign_key_constraint is not None:
            header += f', FOREIGN KEY ({self.foreign_key_constraint.id_name}) REFERENCES {self.foreign_key_constraint.reference_table_name}({self.foreign_key_constraint.reference_id_name})'

            # Add on delete cascade constraint
            if self.foreign_key_constraint.is_set_null_active_on_delete:
                header += ' ON DELETE SET NULL'

        return header

    @staticmethod
    def createHeaders(*args: 'TableItem') -> str:
        """
        This method creates headers from given list of table items
        """
        return ', '.join([item.generateHeader() for item in args])

    @staticmethod
    def generateTableItem(game_object: Coin | Player):
        """
        This method generates table items list of given game object
        """
        attributes: list = game_object.getAttributes()
        datatypes: dict = game_object.getDatatypesWithAttributes()
        table_items: list[TableItem] = []

        Guard.againstDifferentLengths(attributes, list(datatypes.values()))

        for i in range(len(attributes)):
            name: str = attributes[i]
            type: DataType = datatypes[name]
            is_primary_key: bool = attributes[i] == game_object.getPrimaryKeyAttribute()

            table_items.append(TableItem(
                name=name, type=type, is_primary_key=is_primary_key
            ))

        return table_items
