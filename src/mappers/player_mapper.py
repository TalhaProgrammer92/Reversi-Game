from mappers.mapper import Mapper
from game_objects.player.player import Player


class PlayerMapper:
    @staticmethod
    def table():
        return Mapper.to_table(Player.table_name(), Player.getAttributesList(), Player.getDatatypes(), Player.getNullableDict(), Player.getForiegnKeyConstraint())
