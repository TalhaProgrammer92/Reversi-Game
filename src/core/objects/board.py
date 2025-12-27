from core.objects.cell import Cell
from core.objects.coin import Coin
from core.misc.position import Position
from core.misc.func import generate_guid
from core.enums.coin_state import CoinState
from core.shield.guard import Guard


class Board:
    """
    Represents the 8x8 Reversi game board.
    Manages the grid of cells and implements core game logic.
    """

    SIZE: int = 8

    # Constructor
    def __init__(self):
        self.__grid: list[list[Cell]] = []

    ###########
    # Getters #
    ###########

    @property
    def grid(self) -> list[list[Cell]]:
        """Returns the grid of cells"""
        return self.__grid

    ################
    # Initialization
    ################

    def initialize(self) -> None:
        """Create 8x8 grid and place initial 4 coins in center"""
        # Create empty grid
        self.__grid = [[Cell() for _ in range(Board.SIZE)] for _ in range(Board.SIZE)]

        # Place initial 4 coins (Reversi starting position)
        # Center positions: (4,4), (4,5), (5,4), (5,5) in 1-indexed
        self.place_coin(Position(4, 4), Coin(generate_guid(), CoinState.WHITE))
        self.place_coin(Position(4, 5), Coin(generate_guid(), CoinState.BLACK))
        self.place_coin(Position(5, 4), Coin(generate_guid(), CoinState.BLACK))
        self.place_coin(Position(5, 5), Coin(generate_guid(), CoinState.WHITE))

    ###############
    # Cell Access #
    ###############

    def get_cell(self, position: Position) -> Cell:
        """Get cell at given position (1-indexed)"""
        Guard.against_none(position, 'position')
        return self.__grid[position.row - 1][position.column - 1]

    def is_within_bounds(self, row: int, column: int) -> bool:
        """Check if coordinates are within board boundaries"""
        return 1 <= row <= Board.SIZE and 1 <= column <= Board.SIZE

    ###################
    # Coin Operations #
    ###################

    def place_coin(self, position: Position, coin: Coin) -> None:
        """Place a coin at specified position"""
        Guard.against_none(position, 'position')
        Guard.against_none(coin, 'coin')

        cell = self.get_cell(position)
        cell.place(coin)
        coin.place(position)

    def remove_coin(self, position: Position) -> Coin | None:
        """Remove and return coin from specified position"""
        Guard.against_none(position, 'position')
        cell = self.get_cell(position)
        return cell.clear()

    ######################
    # Reversi Game Logic #
    ######################

    def get_coins_to_flip(self, position: Position, state: CoinState) -> list[Position]:
        """Get list of opponent coins that would be flipped by placing at position"""
        # 8 directions: N, NE, E, SE, S, SW, W, NW
        directions = [
            (-1, 0),   # North
            (-1, 1),   # North-East
            (0, 1),    # East
            (1, 1),    # South-East
            (1, 0),    # South
            (1, -1),   # South-West
            (0, -1),   # West
            (-1, -1)   # North-West
        ]

        coins_to_flip: list[Position] = []

        for dr, dc in directions:
            coins_to_flip.extend(self.__check_direction(position, state, dr, dc))

        return coins_to_flip

    def __check_direction(self, position: Position, state: CoinState, dr: int, dc: int) -> list[Position]:
        """Checks one direction for flippable coins"""
        row, col = position.row + dr, position.column + dc
        temp_flips: list[Position] = []

        while self.is_within_bounds(row, col):
            cell = self.__grid[row - 1][col - 1]

            if cell.is_empty:
                return []  # Gap found, no flip possible
            elif cell.state == state:
                return temp_flips  # Found our coin, return collected flips
            else:
                temp_flips.append(Position(row, col))  # Opponent coin, add to potential flips

            row += dr
            col += dc

        return []  # Reached edge without finding our coin

    def is_valid_move(self, position: Position, state: CoinState) -> bool:
        """Check if placing a coin at position is valid for given player"""
        cell = self.get_cell(position)

        # Cell must be empty
        if cell.is_occupied:
            return False

        # Must flip at least one opponent coin
        return len(self.get_coins_to_flip(position, state)) > 0

    def get_valid_moves(self, state: CoinState) -> list[Position]:
        """Get all valid move positions for a player"""
        valid_moves: list[Position] = []

        for row in range(1, Board.SIZE + 1):
            for col in range(1, Board.SIZE + 1):
                pos = Position(row, col)
                if self.is_valid_move(pos, state):
                    valid_moves.append(pos)

        return valid_moves

    def execute_move(self, position: Position, coin: Coin) -> int:
        """Place coin and flip all captured coins. Returns number of flips."""
        Guard.against_none(position, 'position')
        Guard.against_none(coin, 'coin')

        # Get coins to flip before placing
        coins_to_flip = self.get_coins_to_flip(position, coin.state)

        # Place the coin
        self.place_coin(position, coin)

        # Flip captured coins
        for flip_pos in coins_to_flip:
            self.get_cell(flip_pos).flip()

        return len(coins_to_flip)

    def has_valid_moves(self, state: CoinState) -> bool:
        """Check if player has any valid moves available"""
        return len(self.get_valid_moves(state)) > 0

    ######################
    # Game State Queries #
    ######################

    def count_coins(self, state: CoinState) -> int:
        """Count coins of a specific state (BLACK/WHITE)"""
        count = 0
        for row in self.__grid:
            for cell in row:
                if cell.state == state:
                    count += 1
        return count

    def count_empty_cells(self) -> int:
        """Count remaining empty cells on the board"""
        count = 0
        for row in self.__grid:
            for cell in row:
                if cell.is_empty:
                    count += 1
        return count

    def is_full(self) -> bool:
        """Check if board has no empty cells"""
        return self.count_empty_cells() == 0

    def get_score(self) -> dict[CoinState, int]:
        """Get score as dictionary {BLACK: count, WHITE: count}"""
        return {
            CoinState.BLACK: self.count_coins(CoinState.BLACK),
            CoinState.WHITE: self.count_coins(CoinState.WHITE)
        }

    def get_winner(self) -> CoinState | None:
        """
        Determine the winner based on coin count.
        Returns None if it's a tie.
        """
        score = self.get_score()
        black_count = score[CoinState.BLACK]
        white_count = score[CoinState.WHITE]

        if black_count > white_count:
            return CoinState.BLACK
        elif white_count > black_count:
            return CoinState.WHITE
        else:
            return None  # Tie

    ###########
    # Display #
    ###########

    def display_in_terminal(self) -> None:
        """Display board in console with grid lines"""
        print("\n    A   B   C   D   E   F   G   H")
        print("  +" + "---+" * Board.SIZE)

        for row_idx, row in enumerate(self.__grid, 1):
            row_str = f"{row_idx} |"
            for cell in row:
                row_str += f" {cell} |"
            print(row_str)
            print("  +" + "---+" * Board.SIZE)

        # Display score
        score = self.get_score()
        print(f"\n  Score: [B] BLACK = {score[CoinState.BLACK]}  |  [W] WHITE = {score[CoinState.WHITE]}")

    def display_with_valid_moves(self, state: CoinState) -> None:
        """Display board highlighting valid moves for player"""
        valid_moves = self.get_valid_moves(state)
        valid_positions = {(pos.row, pos.column) for pos in valid_moves}

        print("\n    A   B   C   D   E   F   G   H")
        print("  +" + "---+" * Board.SIZE)

        for row_idx, row in enumerate(self.__grid, 1):
            row_str = f"{row_idx} |"
            for col_idx, cell in enumerate(row, 1):
                if (row_idx, col_idx) in valid_positions:
                    row_str += " * |"  # Valid move marker
                else:
                    row_str += f" {cell} |"
            print(row_str)
            print("  +" + "---+" * Board.SIZE)

        # Display score and valid move count
        score = self.get_score()
        player_name = "BLACK" if state == CoinState.BLACK else "WHITE"
        print(f"\n  Score: [B] BLACK = {score[CoinState.BLACK]}  |  [W] WHITE = {score[CoinState.WHITE]}")
        print(f"  {player_name}'s turn - {len(valid_moves)} valid moves available (* marks)")

    def __repr__(self) -> str:
        """String representation of the board"""
        score = self.get_score()
        return f"Board(BLACK: {score[CoinState.BLACK]} | WHITE: {score[CoinState.WHITE]})"
