from data.handlers.database.database_connection import DatabaseConnection
from data.handlers.database.database_manager import DatabaseManager
from data.handlers.json_manager import load_json
from data.handlers.common.table_item import TableItem
from game_objects.player.player import Player
from enums.player.player_attribute import PlayerAttribute
from enums.data_handler.data_type import DataType
from pathlib import Path
from os.path import join as jp


if __name__ == '__main__':
    json = load_json(Path(__file__).parent / "settings" / "database_connections.json")
    path = jp(json['general']['path'], json['general']['file'])

    connection: DatabaseConnection = DatabaseConnection(path=path)

    player: Player = Player(id=1, username="Talha Ahmad", score=0, credits=100)
    attributes: dict = player.getAttributesDict()
    datatypes: dict = player.getDatatypesWithAttributes()
    items: list[TableItem] = [
        TableItem(
            name=attributes[PlayerAttribute.ID],
            type=DataType.INTEGER,
            is_primary_key=True
        )
    ]
    items.extend([TableItem(
        name=attributes[i],
        type=datatypes[i],
        nullable=False
    ) for i in range(1, len(datatypes.values()))])

    try:
        DatabaseManager.createTable(
            table_name=Player.table_name(),
            table_items=[item for item in items],
            db_conn=connection
        )
    except Exception as e:
        print(e)
