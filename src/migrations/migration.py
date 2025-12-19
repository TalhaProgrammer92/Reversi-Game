from data.handlers.common.table_item import TableItem
from dependencies.config_database import ConfigDatabase
from data.handlers.database.database_connection import DatabaseConnection
from game_objects.player.player import Player
from mappers.player_mapper import PlayerMapper


class MigrationBuilder:
    def __init__(self, connection: DatabaseConnection):
        self._config: ConfigDatabase = ConfigDatabase(connection)
        self._connection: DatabaseConnection = connection

    def createTable(self, name: str, table: list[TableItem]):
        self._config.addTable(name, table)

    def build(self):
        self._config.creatAllTables()


class Migration(MigrationBuilder):
    def __init__(self, connection: DatabaseConnection):
        super().__init__(connection)

    def up(self) -> None:
        self.createTable(
            name=Player.table_name(),
            table=PlayerMapper.table()
        )
