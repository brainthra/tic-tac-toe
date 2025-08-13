# engine/board.py

from typing import List, Optional, Tuple

class Board:
    def __init__(self) -> None:
        # ' ' = empty, 'X' or 'O' = players
        self.state: List[str] = [' '] * 9
        self.current_player: str = 'X'

    def copy(self) -> "Board":
        new_board = Board()
        new_board.state = self.state.copy()
        new_board.current_player = self.current_player
        return new_board

    def legal_moves(self) -> List[int]:
        """Return a list of empty positions [0..8]."""
        return [i for i, cell in enumerate(self.state) if cell == ' ']

    def apply_move(self, move: int) -> None:
        """Place the current player's mark on the board at position `move`."""
        if self.state[move] != ' ':
            raise ValueError(f"Cell {move} is already occupied.")
        self.state[move] = self.current_player
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def is_full(self) -> bool:
        return all(cell != ' ' for cell in self.state)

    def winner(self) -> Optional[str]:
        """Return 'X', 'O', or None if no winner yet."""
        wins: List[Tuple[int, int, int]] = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # cols
            (0, 4, 8), (2, 4, 6)               # diagonals
        ]
        for a, b, c in wins:
            if self.state[a] != ' ' and self.state[a] == self.state[b] == self.state[c]:
                return self.state[a]
        return None

    def is_terminal(self) -> bool:
        """Game over if board full or someone has won."""
        return self.winner() is not None or self.is_full()

    def __str__(self) -> str:
        """Human-readable board layout."""
        rows = [
            f" {self.state[0]} | {self.state[1]} | {self.state[2]} ",
            "---+---+---",
            f" {self.state[3]} | {self.state[4]} | {self.state[5]} ",
            "---+---+---",
            f" {self.state[6]} | {self.state[7]} | {self.state[8]} ",
        ]
        return "\n".join(rows)
