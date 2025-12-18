from data.handlers.common.table_item import TableItem
from dependencies.config_database import ConfigDatabase
from data.handlers.database.database_connection import DatabaseConnection


class MigrationBuilder:
    def __init__(self, config: ConfigDatabase, connection: DatabaseConnection):
        self.config: ConfigDatabase = config
        self.connection: DatabaseConnection = connection
