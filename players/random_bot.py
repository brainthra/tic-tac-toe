# players/random_bot.py
import random
from engine.board import Board
from .base import Player

class RandomBot(Player):
    """Baseline: choose uniformly among legal moves."""

    def __init__(self, seed: int | None = None) -> None:
        self._rng = random.Random(seed)

    def choose_move(self, board: Board) -> int:
        moves = board.legal_moves()
        if not moves:
            raise RuntimeError("No legal moves available.")
        return self._rng.choice(moves)
