from mappers.mapper import Mapper
from game_objects.player.player import Player


class PlayerMapper:
    @staticmethod
    def table():
        """
        This method maps player entity (game object) with a list of table items i.e. table
        """
        return Mapper.to_table(
            name=Player.table_name(),
            attributes=Player.getAttributesList(),
            datatypes=Player.getDatatypes(),
            nullable=Player.getNullableDict(),
            primary_key=Player.getPrimaryKey(),
            foreign_key=Player.getForiegnKeyConstraint()
        )
