# tests/test_rules_bot.py
from engine.board import Board
from players.rules_bot import RulesBot


def test_winning_move_taken() -> None:
    b = Board()
    b.state = ["X", "X", " ", " ", "O", " ", " ", " ", "O"]
    b.current_player = "X"
    bot = RulesBot()
    mv = bot.choose_move(b)
    assert mv == 2  # Complete the top row


def test_blocking_move_taken() -> None:
    b = Board()
    b.state = ["O", "O", " ", " ", "X", " ", " ", " ", "X"]
    b.current_player = "X"
    bot = RulesBot()
    mv = bot.choose_move(b)
    assert mv == 2  # Block O's win


def test_center_priority() -> None:
    b = Board()
    b.state = ["X", " ", " ", " ", " ", " ", " ", " ", " "]
    b.current_player = "O"
    bot = RulesBot()
    mv = bot.choose_move(b)
    assert mv == 4  # Take center


def test_corner_priority() -> None:
    b = Board()
    b.state = ["X", " ", " ", " ", "O", " ", " ", " ", " "]
    b.current_player = "X"
    bot = RulesBot()
    mv = bot.choose_move(b)
    assert mv in [2, 6, 8]  # Choose a corner (0 is already X)
