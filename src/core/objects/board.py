from core.enums.cell_state import CellState
from core.enums.coin_state import CoinState
from core.enums.direction import Direction
from core.misc.func import generate_guid
from core.misc.position import Position
from core.shield.guard import Guard
from core.objects.cell import Cell
from core.objects.coin import Coin
from core.misc.exceptions import *
from core.misc.size import Size


class Board:
    """
    Represents the 8x8 Reversi game board.
    Manages the grid of cells and implements core game logic.
    """

    # Constructor
    def __init__(self):
        self.__grid: list[list[Cell]] = []

    ###########
    # Getters #
    ###########

    @property
    def size(self) -> Size:
        return Size(8, 8)

    @property
    def area(self) -> int:
        return self.size.row * self.size.column

    @property
    def grid(self) -> list[list[Cell]]:
        """Returns the grid of cells"""
        return self.__grid

    @property
    def is_full(self) -> bool:
        coins: dict = self.get_number_of_coins()
        return coins[CoinState.WHITE] + coins[CoinState.BLACK] == self.area

    #################
    # Board Methods #
    #################

    def initialize(self) -> None:
        """Create 8x8 grid and place initial 4 coins in center"""
        # Create empty grid
        self.__grid = [[Cell() for _ in range(self.size.row)] for _ in range(self.size.column)]

        # Place initial 4 coins (Reversi starting position)
        # Center positions: (4,4), (4,5), (5,4), (5,5) in 1-indexed
        self.place_coin(Position(4, 4), Coin(generate_guid(), CoinState.WHITE))
        self.place_coin(Position(4, 5), Coin(generate_guid(), CoinState.BLACK))
        self.place_coin(Position(5, 4), Coin(generate_guid(), CoinState.BLACK))
        self.place_coin(Position(5, 5), Coin(generate_guid(), CoinState.WHITE))

    def clear(self) -> None:
        """Clears the board and remove all coins"""
        for i in range(self.size.row):
            for j in range(self.size.column):
                self.__grid[i][j].clear()

    ###############
    # Cell Access #
    ###############

    def cell_state(self, position: Position) -> CellState:
        """Get state of the specified cell"""
        self.guard_within_bounds(position)

        return self.get_cell(position).state

    def get_cell(self, position: Position) -> Cell:
        """Get cell at given position (1-indexed)"""
        self.guard_within_bounds(position)

        return self.__grid[position.row - 1][position.column - 1]

    def guard_within_bounds(self, position: Position) -> None:
        """Check if coordinates are within board boundaries"""
        Guard.against_out_of_range(position.row, Position.range(), 'row')
        Guard.against_out_of_range(position.column, Position.range(), 'column')

    def guard_board_initialization(self) -> None:
        """Check if board is not initialized"""
        if len(self.__grid) == 0:
            raise OperationException("The board is not initialized")

    ###################
    # Coin Operations #
    ###################

    def place_coin(self, position: Position, coin: Coin) -> None:
        """Place a coin at specified position"""
        self.guard_board_initialization()
        self.guard_within_bounds(position)

        # Check move validity and flip all coins at possible position based on all directions
        is_valid_move: bool = True if Coin.placing_at_corner(position) else False
        for direction in [
            Direction.TOP, Direction.BOTTOM, Direction.LEFT, Direction.RIGHT,   # Horizontal + Vertical
            Direction.TOP_LEFT, Direction.TOP_RIGHT, Direction.BOTTOM_LEFT, Direction.BOTTOM_RIGHT  # Diagonal
        ]:
            flipped: bool = self.flip_coins(position, coin.state, direction)
            if flipped: # If any coin is flipped then the move is valid
                is_valid_move = True

        # If the move is not valid
        if not is_valid_move:
            raise OperationException(f"Invalid move for the given coin at position {position}")

        # Place the coin
        self.get_cell(position).place(coin)
        coin.place(position)

    def flip_coin(self, position: Position) -> None:
        """Flip a coin at specified position"""
        self.guard_board_initialization()
        self.guard_within_bounds(position)

        self.get_cell(position).flip()

    def remove_coin(self, position: Position) -> Coin | None:
        """Remove and return coin from specified position"""
        self.guard_board_initialization()
        self.guard_within_bounds(position)

        cell = self.get_cell(position)
        return cell.clear()

    def get_number_of_coins(self) -> dict[CoinState, int]:
        """Get the number of coins on the board"""
        coins: dict[CoinState, int] = {
            CoinState.WHITE: 0,
            CoinState.BLACK: 0
        }

        for row in self.__grid:
            for cell in row:
                if cell.state == CellState.OCCUPIED:
                    coins[cell.coin.state] = coins[cell.coin.state] + 1

        return coins

    def flip_coins(self, position: Position, coin_state: CoinState, direction: Direction) -> bool:
        """Flip all coins placed at specified direction based on the given coin's position"""
        pos: Position = position + direction.value
        flip_positions: list[Position] = []

        # Get coin positions to be flipped
        while self.cell_state(pos) == CellState.OCCUPIED and self.get_cell(pos).coin.state != coin_state:
            try:
                flip_positions.append(pos)
                pos += direction.value
            except OutOfRangeException:
                return False    # Because the position has gone out of cell range

        # Flip the coins
        for p in flip_positions:
            self.flip_coin(p)

        return True

    def __repr__(self) -> str:
        """String representation of the board"""
        return '\n'.join([' | '.join([f"{cell}" for cell in self.__grid[i]]) for i in range(self.size.row)])
