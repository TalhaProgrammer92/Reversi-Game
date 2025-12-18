from data.handlers.common.table_item import TableItem
from data.handlers.common.foreign_key_constraint import ForeignKeyConstraint
from enums.data_handler.data_type import DataType
from shield.guard import Guard


class Mapper:
    @staticmethod
    def to_table(self, name: str, attributes: list, datatypes: dict, nullable: dict, primary_key, foreign_key: ForeignKeyConstraint | None = None) -> list[TableItem]:
        """
        This method creates a table based on the parameters
        """
        # Guard against empty values
        Guard.againstEmpty(name, 'table name')
        Guard.againstEmpty(attributes, 'table columns')

        # Get primary key attribute
        primary_key_atr_index: int = attributes.index(primary_key)
        primary_key_attribute = attributes[primary_key_atr_index]

        # Table items list
        table_items: list[TableItem] = [
            # Primary Key - Constraint
            TableItem(
                name=primary_key_attribute.value,
                type=datatypes[primary_key_attribute],
                is_primary_key=True
            )
        ]

        # Pop the primary key which is already being added previously
        attributes = attributes.pop(primary_key_atr_index)

        # Add other attributes to the table
        for attribute in attributes:
            table_items.append(TableItem(
                name=attribute.value,
                type=datatypes[attribute],
                nullable=nullable[attribute]
            ))

        # Add -  Foreign Key - Constraint
        if foreign_key:
            table_items.append(TableItem(
                name=foreign_key.id_name,
                type=DataType.INTEGER,
                foreign_key=foreign_key
            ))

        return table_items
