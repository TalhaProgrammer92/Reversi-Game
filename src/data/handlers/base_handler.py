from xml.sax.handler import property_interning_dict

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


class DatabaseConnection:
    def __init__(self):
        self.__database: sq.Connection = sq.connect(path.join(settings.data['path'], settings.data['connection']))
        self.__cursor: sq.Cursor = self.__database.cursor()

    @property
    def database(self) -> sq.Connection:
        return self.__database

    @property
    def cursor(self) -> sq.Cursor:
        return self.__cursor


class ForeignKeyConstraint:
    def __init__(self, **kwargs):
        self.__id_name: str = kwargs.get('id_name', '')
        self.__reference: str = kwargs.get('reference_table', '')
        self.__on_delete_set_null: bool = kwargs.get('on_delete_set_null', False)

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
    def reference_table(self) -> str:
        return self.__reference

    @property
    def is_set_null_active_on_delete(self) -> bool:
        return self.__on_delete_set_null


class TableItem:
    def __init__(self, **kwargs):
        self.__name: str = kwargs.get('name', 'title')
        self.__nullable: bool = kwargs.get('nullable', True)
        self.__data_type: DataType = kwargs.get('type', DataType.NULL)
        self.__is_primary_key: bool = kwargs.get('is_primary_key', False)
        self.__foreign_key_constraint: ForeignKeyConstraint | None = kwargs.get('foreign_key', None)

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

    def generateHeader(self) -> str:
        header: str = ''

        pass

        return header


class DatabaseManager:
    @staticmethod
    def createTable(table_name: str, table_items: list[TableItem], db_conn: DatabaseConnection):
        pass
