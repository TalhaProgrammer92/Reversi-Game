from data.handlers.common.table_item import TableItem
from data.handlers.database.database_manager import DatabaseManager, DatabaseConnection
from shield.guard import Guard


class ConfigDatabase:
    def __init__(self, connection: DatabaseConnection):
        self.connection: DatabaseConnection = connection
        self.__tables: dict[str, list[TableItem]] = {}

    def addTable(self, name: str, table: list[TableItem]):
        """
        This method adds a new table in the dictionary
        """
        Guard.againstEmpty(name, 'table name')
        Guard.againstEmpty(table, 'table items')

        self.__tables[name] = table

    def creatAllTables(self):
        """
        This method creates all tables available in "self.__tables"
        """
        for name, attributes in self.__tables:
            DatabaseManager.createTable(
                table_name=name,
                table_items=attributes,
                database_connection=self.connection
            )
