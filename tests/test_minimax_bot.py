# tests/test_minimax_bot.py
from engine.board import Board
from players.minimax_bot import MinimaxBot
from players.rules_bot import RulesBot


def test_minimax_blocks_win() -> None:
    b = Board()
    b.state = ["O", "O", " ", " ", "X", " ", " ", " ", "X"]
    b.current_player = "X"
    bot = MinimaxBot()
    mv = bot.choose_move(b)
    assert mv == 2  # block O's win


def test_minimax_wins_when_possible() -> None:
    b = Board()
    b.state = ["X", "X", " ", " ", "O", " ", " ", " ", "O"]
    b.current_player = "X"
    bot = MinimaxBot()
    mv = bot.choose_move(b)
    assert mv == 2  # win immediately


def test_minimax_vs_rules() -> None:
    # Minimax should never lose to RulesBot
    minimax = MinimaxBot()
    rules = RulesBot()
    x_wins = o_wins = draws = 0
    games = 10
    for _ in range(games):
        b = Board()
        while not b.is_terminal():
            current = minimax if b.current_player == "X" else rules
            b.apply_move(current.choose_move(b))
        winner = b.winner()
        if winner == "X":
            x_wins += 1
        elif winner == "O":
            o_wins += 1
        else:
            draws += 1
    assert o_wins == 0
