import settings
import sqlite3 as sq
import os.path as path
from game_objects.player.player import *
from data.handlers.common import *


class DatabaseConnection:
    def __init__(self):
        self.__database: sq.Connection = sq.connect(path.join(settings.data['path'], settings.data['connection']))
        self.__cursor: sq.Cursor = self.__database.cursor()

    def executeAndCommit(self, query: str) -> None:
        """
        This method executes the given query and commit
        """
        self.__cursor.execute(query)
        self.__database.commit()

    def commit(self) -> None:
        self.__database.commit()

    def fetchone(self, query: str) -> list:
        """
        This method executes the given query and return data
        """
        self.__cursor.execute(query)
        return self.__cursor.fetchone()


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
        header: str = f"{self.name} {self.data_type.name}"

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


class DatabaseManager:
    @staticmethod
    def createTable(table_name: str, table_items: list[TableItem], db_conn: DatabaseConnection | None = None) -> None:
        """
        This method creates a table inside database if it doesn't exist
        """
        query: str = f"CREATE TABLE IF NOT EXISTS {table_name}({', '.join([item.generateHeader() for item in table_items])})"
        print(query)    # Debugging
        # db_conn.executeAndCommit(query)

    @staticmethod
    def deleteTable(table_name: str, db_conn: DatabaseConnection | None = None) -> None:
        """
        This method deletes a particular table inside the given database
        """
        query: str = f'DROP TABLE {table_name};'
        print(query)    # Debugging
        # db_conn.executeAndCommit(query)

    @staticmethod
    def insertData(table_name: str, data_values_name: tuple[str], data_values: tuple, db_conn: DatabaseConnection | None = None) -> None:
        """
        This method inserts data into a particular table of the given database
        """
        query: str = f'INSERT INTO {table_name} {data_values_name} VALUES {data_values}'
        print(query)    # Debugging
        # db_conn.executeAndCommit(query)

    @staticmethod
    def retrieveData(table_name: str, attributes: list, condition: DataCondition | None, db_conn: DatabaseConnection | None = None, commit: bool = False) -> list:
        """
        This method retrieves data from a particular table of the given database
        """
        query: str = f'SELECT {','.join(attributes)} FROM {table_name}'

        # Add condition
        if condition is not None:
            query += f' WHERE {condition.getConditionString()};'
        print(query)    # Debugging
        # Fetch data from the database
        # data: list = db_conn.fetchone(query)
        # if commit:
        #     db_conn.commit()
        #
        # return data
        return []

    @staticmethod
    def updateData(table_name: str, attributes: list[str], values: list[str], condition: DataCondition | None, db_conn: DatabaseConnection | None = None) -> None:
        """
        This method updates particular data from a table of the given database
        """
        query = f'UPDATE {table_name} SET ' + ','.join([f"{attributes[i]} = {values[i]}" for i in range(len(attributes))])

        if condition is not None:
            query += f" WHERE {condition.getConditionString()};"
        print(query)    # Debugging
        # db_conn.executeAndCommit(query)

    @staticmethod
    def removeData(table_name: str, condition: DataCondition | None, db_conn: DatabaseConnection | None = None) -> None:
        """
        This method removes data from a table on given condition
        """
        query = f"DELETE FROM {table_name}"

        if condition is not None:
            query += f" WHERE {condition.getConditionString()};"
        print(query)    # Debugging
        # db_conn.executeAndCommit(query)

# Testing - Code
if __name__ == '__main__':
    # Get data-types dictionary
    types: dict = Player.getDatatypesWithAttributes()

    # Get attributes of and create TableItem list
    attributes: dict = Player.getAttributesDict()
    table_items: list[TableItem] = [TableItem(
        name=attributes[PlayerAttribute.ID],
        type=types[PlayerAttribute.ID],
        is_primary_key=True
    )]
    attributes_values: list = list(attributes.values())
    table_items.extend([
        TableItem(
            name=attributes_values[i],
            type=types[attributes_values[i]],
            nullable=False
        ) for i in range(1, len(attributes_values))
    ])

    # Generate query to create table
    DatabaseManager.createTable(
        table_name=Player.table_name(),
        table_items=table_items
    )
