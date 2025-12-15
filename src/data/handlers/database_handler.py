import settings
import sqlite3 as sq
import os.path as path
from enum import Enum


class DataType(Enum):
    NULL = 0        # The value is a NULL value.
    TEXT = 1        # Best for strings of any length (names, descriptions, etc.).
    REAL = 2        # Best for floating-point numbers and decimal values.
    INTEGER = 3     # Best for whole numbers, including primary keys (ID columns). Uses 1 to 8 bytes.
    NUMERIC = 4     # General purpose; can store any of the four types. Often used for DECIMAL or BOOLEAN.
    BLOB = 5        # For storing raw data like images, audio files, or serialized objects.


class OperatorComparison(Enum):
    EQUAL_TO = '='
    NOT_EQUAL_TO = '!='
    GREATER_THAN = '>'
    LESS_THAN = '<'
    GREATER_EQUAL_TO = '>='
    LESS_EQUAL_TO = '<='


class LogicalComparison(Enum):
    AND = 'and'
    OR = 'or'


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


class DataCondition:
    def __init__(self, **kwargs):
        self.__attribute: str = kwargs.get('attribute', 'num')
        self.__operator: OperatorComparison = kwargs.get('operator', OperatorComparison.EQUAL_TO)
        self.__value: str = kwargs.get('value', '0')

    @staticmethod
    def create(logical_operator: LogicalComparison | None, conditions: list['DataCondition']) -> str:
        """
        This method returns a string for a list of comparisons with logical operators
        """
        if logical_operator is None:
            if len(conditions) == 1:
                return conditions[0].getConditionString()
            else:
                raise Exception("You must enter a logical comparison operator for multiple conditions")

        if len(conditions) == 0:
            raise Exception("Conditions list can't be empty")

        return logical_operator.value.join([condition.getConditionString() for condition in conditions])

    def getConditionString(self) -> str:
        return f"{self.__attribute} {self.__operator.value} {self.__value}"


class ForeignKeyConstraint:
    def __init__(self, **kwargs):
        self.__id_name: str = kwargs.get('id_name', 'foreign_id')
        self.__reference: str = kwargs.get('reference_table', 'foreign')
        self.__reference_id: str = kwargs.get('reference_id', 'id')
        self.__on_delete_set_null: bool = kwargs.get('on_delete_set_null', True)

    ###########
    # Getters #
    ###########
    @property
    def id_name(self) -> str:
        return self.__id_name

    @property
    def id_type(self) -> DataType:
        return DataType.INTEGER

    @property
    def reference_table_name(self) -> str:
        return self.__reference

    @property
    def reference_id_name(self) -> str:
        return self.__reference_id

    @property
    def is_set_null_active_on_delete(self) -> bool:
        return self.__on_delete_set_null


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
    def createTable(table_name: str, table_items: list[TableItem], db_conn: DatabaseConnection) -> None:
        """
        This method creates a table inside database if it doesn't exist
        """
        query: str = f'CREATE TABLE IF NOT EXISTS {table_name}(' + ','.join([item.generateHeader() for item in table_items]) + ')'
        db_conn.executeAndCommit(query)

    @staticmethod
    def deleteTable(table_name: str, db_conn: DatabaseConnection) -> None:
        """
        This method deletes a particular table inside the given database
        """
        query: str = f'DROP TABLE {table_name};'
        db_conn.executeAndCommit(query)

    @staticmethod
    def insertData(table_name: str, data_values_name: tuple[str], data_values: tuple, db_conn: DatabaseConnection) -> None:
        """
        This method inserts data into a particular table of the given database
        """
        query: str = f'INSERT INTO {table_name} {data_values_name} VALUES {data_values}'
        db_conn.executeAndCommit(query)

    @staticmethod
    def retrieveData(table_name: str, attributes: list, condition: DataCondition | None, db_conn: DatabaseConnection, commit: bool = False) -> list:
        """
        This method retrieves data from a particular table of the given database
        """
        query: str = f'SELECT {','.join(attributes)} FROM {table_name}'

        # Add condition
        if condition is not None:
            query += f'WHERE {condition.getConditionString()};'

        # Fetch data from the database
        data: list = db_conn.fetchone(query)
        if commit:
            db_conn.commit()

        return data

    @staticmethod
    def updateData(table_name: str, attributes: list[str], values: list[str], condition: DataCondition | None, db_conn: DatabaseConnection) -> None:
        """
        This method updates particular data from a table of the given database
        """
        query = f'UPDATE {table_name} SET ' + ','.join([f"{attributes[i]} = {values[i]}" for i in range(len(attributes))])

        if condition is not None:
            query += f"WHERE {condition.getConditionString()};"

        db_conn.executeAndCommit(query)

    @staticmethod
    def removeData(table_name: str, condition: DataCondition | None, db_conn: DatabaseConnection) -> None:
        """
        This method removes data from a table on given condition
        """
        query = f"DELETE FROM {table_name}"

        if condition is not None:
            query += f" WHERE {condition.getConditionString()};"

        db_conn.executeAndCommit(query)
