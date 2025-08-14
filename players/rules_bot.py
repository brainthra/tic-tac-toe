# players/rules_bot.py
from engine.board import Board

from .base import Player


class RulesBot(Player):
    """Heuristic-based player with simple priorities:
    1. Win immediately if possible.
    2. Block opponent's immediate win.
    3. Take center if free.
    4. Take a corner if free.
    5. Otherwise take any side.
    """

    def choose_move(self, board: Board) -> int:
        moves = board.legal_moves()

        # 1. Win now
        for mv in moves:
            if self._would_win(board, mv, board.current_player):
                return mv

        # 2. Block opponent
        opponent = "O" if board.current_player == "X" else "X"
        for mv in moves:
            if self._would_win(board, mv, opponent):
                return mv

        # 3. Center
        if 4 in moves:
            return 4

        # 4. Corner
        for mv in [0, 2, 6, 8]:
            if mv in moves:
                return mv

        # 5. Side
        return moves[0]

    def _would_win(self, board: Board, move: int, player: str) -> bool:
        test_board = board.copy()
        test_board.state[move] = player
        return test_board.winner() == player
