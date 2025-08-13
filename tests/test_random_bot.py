# tests/test_random_bot.py
from engine.board import Board
from players.random_bot import RandomBot

def test_random_bot_picks_legal_moves():
    b = Board()
    bot = RandomBot(seed=123)
    for _ in range(3):
        mv = bot.choose_move(b)
        assert mv in b.legal_moves()
        b.apply_move(mv)

def test_random_vs_random_completes_game():
    b = Board()
    x = RandomBot(seed=1)
    o = RandomBot(seed=2)
    while not b.is_terminal():
        current = x if b.current_player == 'X' else o
        b.apply_move(current.choose_move(b))
    assert b.is_terminal()
    # winner can be X, O, or None (draw); just ensure game ends within 9 moves
    assert len([c for c in b.state if c != ' ']) <= 9
