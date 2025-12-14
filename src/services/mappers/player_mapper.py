from dtos.player_dtos.player_dto import PlayerDTO
from game_objects.player.player import Player


class PlayerMapper:
    @staticmethod
    def to_dto(player: Player) -> PlayerDTO:
        return PlayerDTO(
            id=player.id,
            username=player.username,
            email=player.email.value,
            score=player.score.value,
            credits=player.credits.value,
            created_at=player.created_at,
            updated_at=player.updated_at
        )
