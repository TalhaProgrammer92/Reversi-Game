# ⚪⚫ Reversi (Othello) Readme

Reversi is a classic abstract strategy board game known for its simple rules but deep complexity.

---

## 💡 Introduction

Reversi is a two-player game played on an **8x8 board**. The objective is for a player to have a **majority** of their colored discs (or pieces) facing up when the last playable empty square is filled.

* **Players:** 2
* **Board:** 8x8 grid (64 squares)
* **Pieces:** 64 identical discs, light on one side (usually white) and dark on the other (usually black).

---

## 📜 Origin and History

Reversi was invented in **1883** in England by Lewis Waterman and John W. Mollett, each claiming to be the original inventor. It gained popularity in Europe in the late 19th century.

However, the game you likely know today is more accurately called **Othello**.

* **Othello:** A popular commercial variant of Reversi, invented in **1971** by **Goro Hasegawa** in Japan. Othello introduced a standard starting position and fixed rules for disc placement, which helped stabilize the game and contributed to its modern global popularity.
* **Name:** The name "Othello" is inspired by Shakespeare's play, referencing the conflict between the Moor (black) and Desdemona (white).

---

## ♟️ Modern Rules of the Game

The rules are straightforward, focusing on "sandwiching" and "flipping" opponent discs.

### 1. Starting the Game

* The board is initially set up with **four discs** in the center:
    * White discs are at positions **d4** and **e5**.
    * Black discs are at positions **e4** and **d5**.
* **Black always moves first.**

### 2. Making a Move

* A move consists of a player placing one disc, with their color facing up, onto any empty square on the board.
* The placed disc **must** "outflank" one or more of the opponent's discs.
    * **Outflanking** means that the opponent's discs are sandwiched between the newly placed disc and another disc of the current player's color, lying in a straight line (horizontally, vertically, or diagonally).

### 3. Flipping Discs

* After placing a disc, the player flips **all** of the opponent's discs that were outflanked in that move. The flipped discs now show the current player's color.

### 4. Passing a Turn

* If a player cannot make a valid move (i.e., they cannot outflank any opponent discs), they **must pass** their turn, and the opponent plays again.

### 5. Ending the Game

* The game ends when **neither player can make a valid move**. This usually happens when:
    * The board is completely filled (64 discs placed).
    * One player has no discs left (a rare outcome).
* The player with the **most discs** of their color on the board wins.

---

## 🧠 Special Techniques (Strategy)

Reversi is a game where short-term gains can lead to long-term losses. Good strategy focuses on control, mobility, and stable positions.

| Technique | Description | Strategic Value |
| :--- | :--- | :--- |
| **Corner Control** | The four corner squares (**a1, a8, h1, h8**) are the most valuable. Discs placed here can **never be flipped**. | **Highest Value.** Guarantees stability and is a major factor in winning. |
| **Edge Play** | The squares along the perimeter (edges) are the second most valuable. They offer greater stability than internal squares. | Focus on acquiring edge positions without giving the opponent the corner. |
| **Avoiding the 'C' and 'X' Squares** | The 'C' squares (e.g., **b1, a2, b8, h7**, etc.) and 'X' squares (e.g., **b2, g2, b7, g7**) are **dangerous** to play early. | Playing here often allows the opponent to take the adjacent highly valuable corner square immediately. |
| **Mobility** | The number of valid moves available to a player. Restricting the opponent's mobility is key. | If the opponent is forced to pass, you get to play consecutive turns. |
| **Parity** | Trying to ensure you are the player who places the **last disc** in a closed-off section of the board. | Important for endgame play, as the last player to move often gets the advantage in a localized area. |
