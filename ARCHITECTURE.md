
---

## 1. Architectural Vision

This project implements **Reversi (Othello)** using a **layered, SOLID-compliant architecture** that supports:

* A **console-based prototype** for rapid validation
* A **Pygame-based graphical interface** for the final experience
* Clean separation between **game rules**, **data**, **presentation**, and **launch mechanisms**
* Future extensibility: AI players, save/load, themes, analytics, networking

The architecture is deliberately designed to ensure that **changing the UI does not require modifying the game logic**, and that **core logic remains testable, deterministic, and UI-agnostic**.

---

## 2. High-Level Directory Structure

```
src/
├─ core/                # Pure game logic and domain rules
│  ├─ enums/
│  ├─ misc/
│  ├─ objects/
│  └─ shield/
│
├─ data/                # Persistence and external data handling
│  ├─ csv_handler/
│  └─ saves/
│     ├─ general/
│     └─ slots/
│
├─ resources/           # Static assets (used only by graphical UI)
│  ├─ music/
│  └─ sprites/
│
├─ prototype/           # Console-based (ANSI) prototype
│  ├─ ansi/
│  └─ launcher/
│
├─ graphical/           # Pygame-based GUI implementation
│  ├─ themes/
│  ├─ launchers/
│  └─ user-settings.json
│
└─ main.py              # Application entrypoint
```

This structure is **intentional and opinionated**:

* `core/` is the **heart of the system**
* `prototype/` and `graphical/` are **replaceable shells**
* `data/` and `resources/` support infrastructure needs without polluting logic

---

## 3. Core Layer (`core/`) — Domain & Rules

### Responsibility

The `core` module contains **pure game logic**.
It must **never**:

* Read input
* Print output
* Access files
* Depend on Pygame, console, or OS features

### Submodules

#### `core/enums/`

Defines all **domain-level enumerations**, for example:

* Player colors (BLACK, WHITE, EMPTY)
* Game phases (RUNNING, FINISHED)
* Directions for board traversal
* Result states (WIN, LOSS, DRAW)

These enums are **shared across all layers**.

---

#### `core/objects/`

Contains the **main domain objects**, such as:

* Board
* Cell / Tile
* Player
* GameState
* Move

These objects:

* Encapsulate rules (e.g., legal move detection, disc flipping)
* Enforce invariants
* Are deterministic and side-effect free (except controlled state mutation)

---

#### `core/misc/`

Utility constructs used internally by the domain:

* Position/value objects
* Direction helpers
* Validation helpers
* Small rule-related helpers

This folder exists to **avoid bloating domain objects** while keeping logic centralized.

---

#### `core/shield/`

Acts as a **protective boundary** around the domain.

Typical use cases:

* Guard clauses
* Preconditions
* Rule enforcement helpers
* Defensive checks to prevent illegal state transitions

The goal is to make **illegal states unrepresentable**.

---

## 4. Data Layer (`data/`) — Persistence & External Storage

### Responsibility

Handles **saving, loading, and exporting game-related data**, without knowing *how the game works*.

### Submodules

#### `data/csv_handler/`

Responsible for:

* CSV-based export/import
* Statistics logging
* Match history analysis
* Debugging or academic analysis

This module never manipulates gameplay directly.

---

#### `data/saves/`

Manages serialized game state.

```
saves/
├─ general/     # Autosaves, checkpoints, last game
└─ slots/       # User-controlled save slots
```

Key principles:

* Save format must be **UI-independent**
* Console and Pygame both load the same saves
* Serialization depends on `core` objects only

---

## 5. Resources (`resources/`) — Static Assets

Used **exclusively by the graphical layer**.

```
resources/
├─ sprites/     # Board tiles, discs, UI icons
└─ music/       # Background music, effects
```

Rules:

* `core/` must never import from `resources/`
* Console prototype ignores this directory entirely

---

## 6. Prototype Layer (`prototype/`) — Console Version

### Purpose

The prototype is a **fast-feedback, low-cost validation layer**.

It is:

* Console-based (ANSI)
* Minimal
* Deterministic
* Easy to debug

### Structure

#### `prototype/ansi/`

Implements:

* Board rendering using ASCII / Unicode
* Highlighting legal moves
* Input parsing (`row col`, `pass`, `quit`)

This layer:

* Translates user input → domain commands
* Translates domain state → text output

---

#### `prototype/launcher/`

Responsible for:

* Wiring domain objects
* Choosing human vs AI players
* Starting the game loop

This keeps startup logic **out of `main.py`**.

---

## 7. Graphical Layer (`graphical/`) — Pygame UI

### Purpose

Provides a **fully interactive graphical experience** using **Pygame**, without touching core logic.

### Structure

#### `graphical/themes/`

Defines:

* Color palettes
* Board styles
* Disc styles
* Fonts

Themes are swappable **without changing game logic**.

---

#### `graphical/launchers/`

Graphical entrypoints:

* Window initialization
* Event loop startup
* Dependency wiring (human vs AI, themes)

Multiple launchers allow:

* Debug mode
* Fullscreen mode
* AI-vs-AI simulations

---

#### `graphical/user-settings.json`

User preferences:

* Resolution
* Theme
* Sound volume
* Animation speed

Loaded only by the graphical layer.

---

## 8. Application Entrypoint (`main.py`)

`main.py` is intentionally **thin**.

Responsibilities:

* Parse startup configuration
* Decide which launcher to run (prototype vs graphical)
* Delegate control immediately

Example decision logic:

* Console during development
* Pygame for final release
* AI-only mode for testing

---

## 9. SOLID & Design Principles Applied

### Single Responsibility

Each folder has **one clear reason to change**:

* Rules → `core`
* UI → `prototype` / `graphical`
* Persistence → `data`

---

### Open / Closed

New UI, AI, or themes are added by **extension**, not modification.

---

### Dependency Inversion

* UI depends on `core`
* `core` depends on nothing
* Data depends on `core`, not vice versa

---

### Strategy Pattern

* AI players
* Themes
* Input methods

---

### Adapter Pattern

* Console adapter
* Pygame adapter
* Future: Network adapter

---

## 10. Console → Pygame Transition Strategy

The workflow is **intentional**:

1. Implement all rules in `core/`
2. Validate gameplay using `prototype/ansi`
3. Lock domain logic with tests
4. Build Pygame UI on top of the same domain
5. Never rewrite rules for graphics

This guarantees:

* No logic duplication
* No UI-driven bugs
* Confidence when scaling features

---

## 11. Testing Strategy

* **Unit tests** → `core` (board logic, move legality)
* **Integration tests** → AI vs AI
* **Manual tests** → console prototype
* **Visual tests** → Pygame UI

The console version acts as a **reference implementation**.

---

## 12. Future Extensions (Planned)

* Minimax / MCTS AI
* Replay system
* Online multiplayer
* Tournament mode
* Visual analytics overlay

All of these fit naturally without restructuring the project.

---

## 13. Summary

This architecture ensures that:

* Game rules are **authoritative and protected**
* UI is **replaceable**
* Prototype accelerates development
* Pygame adds polish, not complexity
* The codebase remains **professional, scalable, and educational**

This is not just a Reversi game —
it is a **reference-quality software architecture exercise**.

---
