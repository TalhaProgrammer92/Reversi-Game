# Architecture proposal for a SOLID, scalable Reversi (Othello) project — console → GUI

Below is a practical, team-friendly architecture and a set of concrete code examples you can clone and extend. The design follows SOLID principles, clean separation of concerns, dependency inversion, testability, and gradual UI replacement: first an ANSI console interface, then swap in a Pygame adapter without changing domain logic.

---

# Project overview & goals

* **Primary purpose:** teach professional engineering practices: separation of concerns, layered architecture, dependency inversion, testing, CI, incremental delivery (console → GUI), and extensibility (AI opponents, networking).
* **High-level constraints:** pure Python 3.11+ (typing), minimal dependencies for console version, optional `pygame` for GUI.
* **Quality goals:** unit tests, static typing (mypy), linting (flake8/ruff), CI pipeline.

---

# High-level architecture (layered)

```
src/
├─ reversi/
│  ├─ domain/           # pure domain logic: rules, board, types, exceptions
│  ├─ application/      # use-cases / services / game engine orchestrator
│  ├─ ports/            # abstract interfaces (repositories, UI ports, event bus)
│  ├─ adapters/         # concrete implementations: console UI, pygame UI, AI strategies
│  ├─ infra/            # infrastructure: logging, config, persistence (if any)
│  └─ cli.py            # entrypoint for console app
tests/
├─ unit/
└─ integration/
```

* **domain:** Entities and business rules. No IO, no presentation.
* **application:** Use cases. Orchestrates domain and calls ports (interfaces).
* **ports:** Define interfaces (abstract base classes) the application depends on — UI, AI, persistence.
* **adapters:** Concrete implementations of ports. Examples: `ConsoleUI`, `PygameUI`, `RandomAI`, `MinimaxAI`.
* **infra:** Logging, configuration, DI wiring.
* **cli.py / gui_launcher.py:** Compose dependencies and start the app.

This is a classic Hexagonal / Ports-and-Adapters approach combined with Clean Architecture.

---

# Key design patterns used

* **Single Responsibility (S)** — each module/class has one reason to change (Board, Rules, Renderer, InputHandler).
* **Open/Closed (O)** — add new UI or AI by adding adapters; core business logic unchanged.
* **Liskov (L)** — interfaces/abstract base classes ensure substitutability (ConsoleUI and PygameUI implement `UIPort`).
* **Interface Segregation (I)** — small focused interfaces: `UIPort`, `MoveValidator`, `AIPlayer`.
* **Dependency Inversion (D)** — application depends on abstract `ports.*` not concrete adapters.
* **Observer / Event Bus** — optional for decoupling UI updates, logging, analytics.
* **Strategy** — swap AI strategies.
* **Command** — optionally for undo/redo move history.

---

# Core domain objects (concepts)

* `Color` enum: BLACK, WHITE, EMPTY
* `Position` (row, col)
* `Board` class: grid, legal move calculations, apply move (flipping discs)
* `Rules` (pure functions or class): determines legal moves & flips
* `GameState` / `GameResult`: current turn, scores, finished flag

Domain must contain **no I/O**.

---

# Example code snippets

Below are compact, directly usable examples illustrating structure and DI. These are intentionally concise; expand and add tests.

## 1) Types and enums (`domain/types.py`)

```python
# src/reversi/domain/types.py
from __future__ import annotations
from enum import Enum
from dataclasses import dataclass

class Color(Enum):
    EMPTY = 0
    BLACK = 1
    WHITE = 2

    def opponent(self) -> "Color":
        if self == Color.BLACK:
            return Color.WHITE
        if self == Color.WHITE:
            return Color.BLACK
        return Color.EMPTY

@dataclass(frozen=True)
class Pos:
    row: int
    col: int
```

## 2) Board & rules (`domain/board.py`)

```python
# src/reversi/domain/board.py
from __future__ import annotations
from typing import List, Iterable, Tuple
from .types import Color, Pos

DIRECTIONS = [( -1,-1), (-1,0), (-1,1),
              ( 0,-1),         ( 0,1),
              ( 1,-1), ( 1,0), ( 1,1)]

class Board:
    SIZE = 8

    def __init__(self):
        self.grid: List[List[Color]] = [[Color.EMPTY]*self.SIZE for _ in range(self.SIZE)]
        # Starting position
        self.grid[3][3] = Color.WHITE
        self.grid[4][4] = Color.WHITE
        self.grid[3][4] = Color.BLACK
        self.grid[4][3] = Color.BLACK

    def in_bounds(self, r: int, c: int) -> bool:
        return 0 <= r < self.SIZE and 0 <= c < self.SIZE

    def get(self, pos: Pos) -> Color:
        return self.grid[pos.row][pos.col]

    def set(self, pos: Pos, color: Color) -> None:
        self.grid[pos.row][pos.col] = color

    def copy(self) -> "Board":
        b = Board.__new__(Board)
        b.grid = [row[:] for row in self.grid]
        return b

    def legal_moves(self, color: Color) -> List[Pos]:
        moves = []
        for r in range(self.SIZE):
            for c in range(self.SIZE):
                if self.grid[r][c] != Color.EMPTY:
                    continue
                if self._would_flip(Pos(r,c), color):
                    moves.append(Pos(r,c))
        return moves

    def _would_flip(self, pos: Pos, color: Color) -> bool:
        return any(self._positions_to_flip_in_dir(pos, color, dr, dc) for dr,dc in DIRECTIONS)

    def _positions_to_flip_in_dir(self, pos: Pos, color: Color, dr: int, dc: int) -> List[Pos]:
        r, c = pos.row + dr, pos.col + dc
        flips: List[Pos] = []
        while self.in_bounds(r,c):
            curr = self.grid[r][c]
            if curr == Color.EMPTY:
                return []
            if curr == color:
                return flips
            flips.append(Pos(r,c))
            r += dr; c += dc
        return []

    def apply_move(self, pos: Pos, color: Color) -> None:
        flips_total: List[Pos] = []
        for dr,dc in DIRECTIONS:
            flips = self._positions_to_flip_in_dir(pos, color, dr, dc)
            flips_total.extend(flips)
        if not flips_total:
            raise ValueError("Illegal move")
        self.set(pos, color)
        for p in flips_total:
            self.set(p, color)

    def score(self) -> Tuple[int,int]:
        black = sum(1 for row in self.grid for v in row if v == Color.BLACK)
        white = sum(1 for row in self.grid for v in row if v == Color.WHITE)
        return black, white
```

## 3) Ports (interfaces) (`ports/ui.py`, `ports/ai.py`, `ports/event_bus.py`)

```python
# src/reversi/ports/ui.py
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Iterable
from reversi.domain.types import Pos, Color
from reversi.domain.board import Board

class UIPort(ABC):
    @abstractmethod
    def render(self, board: Board, legal_moves: Iterable[Pos], current: Color) -> None:
        pass

    @abstractmethod
    def request_move(self, legal_moves: Iterable[Pos], current: Color) -> Pos | None:
        """Return chosen Pos or None for pass/quit"""
        pass
```

```python
# src/reversi/ports/ai.py
from __future__ import annotations
from abc import ABC, abstractmethod
from reversi.domain.types import Color, Pos
from reversi.domain.board import Board
from typing import Optional, Iterable

class AIPlayer(ABC):
    @abstractmethod
    def choose_move(self, board: Board, color: Color, legal_moves: Iterable[Pos]) -> Optional[Pos]:
        pass
```

## 4) Application / Game engine (`application/game_service.py`)

```python
# src/reversi/application/game_service.py
from typing import Iterable, Optional
from reversi.domain.board import Board
from reversi.domain.types import Color, Pos
from reversi.ports.ui import UIPort
from reversi.ports.ai import AIPlayer

class GameService:
    def __init__(self, ui: UIPort, black_ai: AIPlayer | None = None, white_ai: AIPlayer | None = None):
        self.ui = ui
        self.board = Board()
        self.current = Color.BLACK
        self.ai_map = {Color.BLACK: black_ai, Color.WHITE: white_ai}

    def run(self) -> None:
        consecutive_passes = 0
        while True:
            legal = self.board.legal_moves(self.current)
            self.ui.render(self.board, legal, self.current)
            if not legal:
                # pass
                consecutive_passes += 1
                if consecutive_passes >= 2:
                    break
                self.current = self.current.opponent()
                continue
            consecutive_passes = 0

            ai = self.ai_map.get(self.current)
            if ai:
                choice = ai.choose_move(self.board.copy(), self.current, legal)
            else:
                choice = self.ui.request_move(legal, self.current)
            if choice is None:  # user requested quit
                break
            self.board.apply_move(choice, self.current)
            self.current = self.current.opponent()

        b,w = self.board.score()
        self.ui.render(self.board, [], self.current)
        # end message
        if b == w:
            self.ui.end_message("Draw", b, w)
        elif b > w:
            self.ui.end_message("Black wins", b, w)
        else:
            self.ui.end_message("White wins", b, w)
```

Add `end_message` to `UIPort`.

## 5) Console UI adapter (ANSI) (`adapters/console_ui.py`)

```python
# src/reversi/adapters/console_ui.py
from typing import Iterable, List
from reversi.ports.ui import UIPort
from reversi.domain.board import Board
from reversi.domain.types import Pos, Color

class ConsoleUI(UIPort):
    def __init__(self):
        # ANSI codes simple helpers
        self.reset = "\x1b[0m"
        self.black_bg = "\x1b[40m"
        self.white_bg = "\x1b[47m"

    def render(self, board: Board, legal_moves: Iterable[Pos], current: Color) -> None:
        moves_set = {(p.row,p.col) for p in legal_moves}
        print("\n  " + " ".join(str(i) for i in range(board.SIZE)))
        for r in range(board.SIZE):
            row_s = []
            for c in range(board.SIZE):
                if (r,c) in moves_set:
                    ch = "*"
                else:
                    v = board.grid[r][c]
                    if v == Color.BLACK:
                        ch = "●"
                    elif v == Color.WHITE:
                        ch = "○"
                    else:
                        ch = "."
                row_s.append(ch)
            print(f"{r} " + " ".join(row_s))
        b,w = board.score()
        print(f"Score — Black: {b}  White: {w}  | Current: {current.name}")

    def request_move(self, legal_moves: Iterable[Pos], current: Color) -> Pos | None:
        legal = {(p.row,p.col) for p in legal_moves}
        while True:
            raw = input("Enter move as 'r c' or 'pass' or 'quit': ").strip().lower()
            if raw in ("quit","q"):
                return None
            if raw in ("pass","p"):
                return None  # our game service treats None as "no move" or we could encode specifically
            try:
                r,c = map(int, raw.split())
                if (r,c) in legal:
                    return Pos(r,c)
                print("Not a legal move.")
            except Exception:
                print("Invalid input.")

    def end_message(self, message: str, black: int, white: int) -> None:
        print(f"Game over: {message}. Final score B:{black} W:{white}")
```

(For passing you may prefer an explicit `Pass` sentinel — keep simple.)

## 6) Simple Random AI (`adapters/random_ai.py`)

```python
# src/reversi/adapters/random_ai.py
import random
from typing import Optional, Iterable
from reversi.ports.ai import AIPlayer
from reversi.domain.types import Pos, Color
from reversi.domain.board import Board

class RandomAI(AIPlayer):
    def choose_move(self, board: Board, color: Color, legal_moves: Iterable[Pos]) -> Optional[Pos]:
        moves = list(legal_moves)
        if not moves:
            return None
        return random.choice(moves)
```

## 7) CLI entrypoint `cli.py`

```python
# src/reversi/cli.py
from reversi.adapters.console_ui import ConsoleUI
from reversi.adapters.random_ai import RandomAI
from reversi.application.game_service import GameService

def main():
    ui = ConsoleUI()
    # Example: one human vs simple AI
    game = GameService(ui=ui, black_ai=None, white_ai=RandomAI())
    game.run()

if __name__ == "__main__":
    main()
```

---

# How this supports console → GUI transition

* `GameService` depends only on `UIPort`. Replace `ConsoleUI` with `PygameUI` that implements the same interface. No change to `Board`, `Rules`, or `GameService`. GUI adapter will provide richer `render` and `request_move` (through event loop).
* AI is swapped similarly via `AIPlayer` implementations.

---

# Additional recommended components

1. **EventBus / Observer** (optional): let UI subscribe to domain events (move played, pass, game_end) — simplifies analytics, logging, and UI updates.
2. **MoveHistory / Command pattern**: to implement undo/redo — store move and flipped discs to reverse a move.
3. **AI module**: multiple strategies:

   * Random
   * Greedy (maximize immediate flips)
   * Minimax with heuristics (corners and mobility)
   * MCTS for advanced students
4. **Network adapter**: implement `NetworkPort` for remote play using sockets or websockets; `GameService` can orchestrate server or client.
5. **Persistence**: optional `GameRepository` port to save/load games (JSON), useful for replay or undo/redo persistence.

---

# Testing & CI

* **Unit tests:** test `Board` flip logic, legal move detection, score calculation.
* **Integration tests:** run a short simulated game between AIs.
* **Linters / type checks:** `ruff`/`flake8`, `mypy`.
* **CI pipeline:** on push/run tests and linters. Use GitHub Actions.

Example unit test outline:

```python
# tests/unit/test_board.py
from reversi.domain.board import Board
from reversi.domain.types import Color, Pos

def test_initial_score():
    b = Board()
    black, white = b.score()
    assert black == 2 and white == 2

def test_simple_flip():
    b = Board()
    # board has center starting setup: black at (3,4)
    b.apply_move(Pos(2,4), Color.BLACK)  # assuming this is legal in test case created
    # assert flipped pieces etc.
```

---

# Repository layout suggestion

```
reversi/                # package root
├─ __init__.py
├─ domain/
│  ├─ __init__.py
│  ├─ types.py
│  └─ board.py
├─ application/
│  └─ game_service.py
├─ ports/
│  ├─ __init__.py
│  ├─ ui.py
│  └─ ai.py
├─ adapters/
│  ├─ __init__.py
│  ├─ console_ui.py
│  ├─ pygame_ui.py        # later
│  ├─ random_ai.py
│  └─ minimax_ai.py
├─ infra/
│  └─ logging.py
└─ cli.py
tests/
pyproject.toml
README.md
```

---

# Team workflow suggestions

* **Split responsibilities**:

  * Developer A: Domain & Rules (board invariants, exhaustive unit tests)
  * Developer B: Application & DI (GameService + ports)
  * Developer A/B: Console UI first (fast feedback loop)
  * After core done: implement AI adapters and Pygame UI in parallel
* **PR rules:** small PRs, each PR must include tests where applicable.
* **Code reviews:** focus on single responsibility, tests, typing.
* **Milestones:**

  1. Board + unit tests (legal moves, flips) — must be green.
  2. GameService + ConsoleUI — playable game.
  3. Add RandomAI + integration tests.
  4. Add stronger AI (minimax) & testing.
  5. Implement Pygame UI adapter & polish UX.
  6. Optional: networking, replay, undo.

---

# Example: How to add Pygame UI (strategy)

* Implement `PygameUI(UIPort)`:

  * Setup window, draw board using rectangles, discs.
  * Maintain event loop; when it's time for `request_move` the UI should block until user clicks a legal square or requests quit.
  * Use the same `render` signature to accept `Board` and `legal_moves`.
* Keep Pygame code inside `adapters/pygame_ui.py` so domain remains pure.

---

# Example: Minimax AI sketch (interface + heuristic)

Minimax should accept a `depth` and heuristic function that evaluates board for color — prefer corners and mobility.

Interface already exists (`AIPlayer`). Implement `MinimaxAI` in `adapters/minimax_ai.py`.

---

# Practical notes & tips

* **Mutability vs immutability:** `Board.copy()` helps AI search without mutating real board.
* **Performance:** Board operations are relatively cheap on 8×8; for deeper AI optimize to bitboards if pursuing performance (later lesson).
* **Logging and debugging:** add `infra/logging.py` and send domain events for tracing.
* **Type hints:** annotate everywhere; helps students learn good habits.
* **Docstrings & README:** document architecture choices and how to run.

---

# Minimal requirements to run console version

`pyproject.toml` with `pytest` for tests. No other dependencies required for console-only.

Run:

```bash
python -m src.reversi.cli
# or
python src/reversi/cli.py
```

---
