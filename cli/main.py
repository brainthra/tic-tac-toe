# cli/main.py
"""
Minimal CLI:
- Human vs Random: python -m cli.main --x human --o random
- Random vs Random: python -m cli.main --x random --o random --seed 42
"""

import argparse
from typing import Any

from engine.board import Board
from players.random_bot import RandomBot
from players.rules_bot import RulesBot


def render(board: Board) -> str:
    s = board.state
    rows = [
        f" {s[0]} | {s[1]} | {s[2]} ",
        "---+---+---",
        f" {s[3]} | {s[4]} | {s[5]} ",
        "---+---+---",
        f" {s[6]} | {s[7]} | {s[8]} ",
    ]
    return "\n".join(rows)


def make_player(kind: str, seed: int | None) -> Any:
    kind = kind.lower()
    if kind == "random":
        return RandomBot(seed=seed)
    if kind == "rules":
        return RulesBot()
    if kind == "human":
        # Return a simple callable object with choose_move(board)
        class Human:
            def choose_move(self, board: Board) -> int:
                while True:
                    try:
                        raw = input("Enter move [0-8]: ").strip()
                        mv = int(raw)
                        if mv in board.legal_moves():
                            return mv
                        print("Illegal move. Try again.")
                    except ValueError:
                        print("Please enter an integer 0-8.")

        return Human()
    raise ValueError(f"Unknown player type: {kind}")


def announce_result(board: Board) -> None:
    w = board.winner()
    if w:
        print(f"\nResult: {w} wins!")
    else:
        print("\nResult: draw.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Play Tic-Tac-Toe in the terminal.")
    parser.add_argument(
        "--x", choices=["human", "random", "rules"], default="human", help="Player X type"
    )
    parser.add_argument(
        "--o", choices=["human", "random", "rules"], default="random", help="Player O type"
    )
    parser.add_argument("--seed", type=int, default=None, help="Random seed (for bots)")
    args = parser.parse_args()

    x_player = make_player(args.x, seed=args.seed)
    o_player = make_player(args.o, seed=args.seed)

    board = Board()
    GRID_HELP = (
        "\nCells are indexed as follows:\n"
        " 0 | 1 | 2 \n"
        "---+---+---\n"
        " 3 | 4 | 5 \n"
        "---+---+---\n"
        " 6 | 7 | 8 \n"
    )
    print(GRID_HELP)

    while not board.is_terminal():
        print(render(board))
        current = x_player if board.current_player == "X" else o_player
        move = current.choose_move(board)
        board.apply_move(move)

    print(render(board))
    announce_result(board)


if __name__ == "__main__":
    main()
