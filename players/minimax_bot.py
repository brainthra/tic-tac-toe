# players/minimax_bot.py
from __future__ import annotations

from engine.board import Board

from .base import Player


class MinimaxBot(Player):
    """Perfect-play Tic-Tac-Toe using classical minimax with alpha-beta pruning.

    Scoring:
        +1 = X wins
         0 = draw
        -1 = O wins

    On each node:
        if board.current_player == 'X' -> maximizing
        if board.current_player == 'O' -> minimizing
    """

    def __init__(self, depth_limit: int | None = None) -> None:
        self.depth_limit = depth_limit

    def choose_move(self, board: Board) -> int:
        moves = board.legal_moves()
        if not moves:
            raise RuntimeError("No legal moves available.")

        maximizing = board.current_player == "X"
        best_score = float("-inf") if maximizing else float("inf")
        best_move = moves[0]

        for move in moves:
            nb = board.copy()
            nb.apply_move(move)
            score = self._minimax(
                nb,
                depth=1,
                alpha=float("-inf"),
                beta=float("inf"),
            )
            if maximizing:
                if score > best_score:
                    best_score, best_move = score, move
            else:
                if score < best_score:
                    best_score, best_move = score, move

        return best_move

    def _utility(self, board: Board) -> float:
        """+1 if X has won, -1 if O has won, 0 otherwise (draw or ongoing)."""
        w = board.winner()
        if w == "X":
            return 1.0
        if w == "O":
            return -1.0
        if board.is_full():
            return 0.0
        # Non-terminal
        return None  # type: ignore[return-value]

    def _minimax(self, board: Board, depth: int, alpha: float, beta: float) -> float:
        # Terminal check
        util = self._utility(board)
        if util is not None:
            return util

        # Depth limit
        if self.depth_limit is not None and depth >= self.depth_limit:
            return self._heuristic(board)

        maximizing = board.current_player == "X"

        if maximizing:
            value = float("-inf")
            for mv in board.legal_moves():
                nb = board.copy()
                nb.apply_move(mv)
                value = max(value, self._minimax(nb, depth + 1, alpha, beta))
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return value
        else:
            value = float("inf")
            for mv in board.legal_moves():
                nb = board.copy()
                nb.apply_move(mv)
                value = min(value, self._minimax(nb, depth + 1, alpha, beta))
                beta = min(beta, value)
                if alpha >= beta:
                    break
            return value

    def _heuristic(self, board: Board) -> float:
        """Cheap eval favoring X (positive) vs O (negative). Only used if depth_limit is set."""
        s = board.state
        lines = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),  # rows
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),  # cols
            (0, 4, 8),
            (2, 4, 6),  # diags
        ]

        score = 0.0
        for a, b, c in lines:
            line = [s[a], s[b], s[c]]
            if "O" not in line:
                score += line.count("X") * 0.3
            if "X" not in line:
                score -= line.count("O") * 0.3

        # positional bias
        if s[4] == "X":
            score += 0.2
        elif s[4] == "O":
            score -= 0.2
        for c in (0, 2, 6, 8):
            if s[c] == "X":
                score += 0.1
            elif s[c] == "O":
                score -= 0.1

        return score
