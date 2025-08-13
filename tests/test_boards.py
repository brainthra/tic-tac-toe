# tests/test_board.py

import pytest

from engine.board import Board


def test_initial_state():
    b = Board()
    assert b.legal_moves() == list(range(9))
    assert b.winner() is None
    assert not b.is_full()
    assert not b.is_terminal()


def test_apply_move_switches_player():
    b = Board()
    b.apply_move(0)
    assert b.state[0] == "X"
    assert b.current_player == "O"


def test_illegal_move_raises():
    b = Board()
    b.apply_move(0)
    with pytest.raises(ValueError):
        b.apply_move(0)


def test_winner_detection_rows():
    b = Board()
    b.state = ["X", "X", "X", " ", " ", " ", " ", " ", " "]
    assert b.winner() == "X"


def test_winner_detection_cols():
    b = Board()
    b.state = ["O", " ", " ", "O", " ", " ", "O", " ", " "]
    assert b.winner() == "O"


def test_winner_detection_diagonals():
    b = Board()
    b.state = ["X", " ", " ", " ", "X", " ", " ", " ", "X"]
    assert b.winner() == "X"


def test_terminal_state_win():
    b = Board()
    b.state = ["X", "X", "X", "O", "O", " ", " ", " ", " "]
    assert b.is_terminal()


def test_terminal_state_draw():
    b = Board()
    b.state = ["X", "O", "X", "X", "O", "O", "O", "X", "X"]
    assert b.is_full()
    assert b.is_terminal()
    assert b.winner() is None
