# tools/tournament.py
from __future__ import annotations

import csv
import itertools
import random
from pathlib import Path

from engine.board import Board
from players.base import Player
from players.minimax_bot import MinimaxBot
from players.random_bot import RandomBot
from players.rules_bot import RulesBot

BOT_CLASSES: dict[str, type[Player]] = {
    "random": RandomBot,
    "rules": RulesBot,
    "minimax": MinimaxBot,
}


def play_game(bot_x: Player, bot_o: Player, seed: int | None = None) -> str:
    """
    Simulates a single game of Tic-Tac-Toe between two bots.

    Args:
        bot_x (Player): The bot playing as 'X'.
        bot_o (Player): The bot playing as 'O'.
        seed (int | None, optional): Seed for RNG to ensure reproducibility. Defaults to None.

    Returns:
        str: The winner of the game ('X', 'O'), or 'draw' if the game ends in a tie.
    """
    random.seed(seed)
    board = Board()
    while not board.is_terminal():
        current = bot_x if board.current_player == "X" else bot_o
        move = current.choose_move(board)
        board.apply_move(move)
    winner = board.winner()
    return winner or "draw"


def run_tournament(
    games_per_pair: int = 100,
    seed: int = 42,
    output_csv: str = "tournaments/tournament_results.csv",
) -> None:
    """
    Runs a round-robin tournament between all pairs of bots defined in BOT_CLASSES,
    playing a specified number of games for each pairing and recording the results.

    For each unique pair of bots (one as X, one as O), plays `games_per_pair` games,
    tracks the number of wins for each bot and draws, and saves the aggregated results
    to a CSV file.

    Args:
        games_per_pair (int): Number of games to play for each bot pairing. Default is 100.
        seed (int): Random seed for reproducibility. Default is 42.
        output_csv (str): Path to the output. Default is "tournaments/tournament_results.csv".

    Returns:
        None
    """
    results = []
    rng = random.Random(seed)
    bot_names = list(BOT_CLASSES.keys())
    for name_x, name_o in itertools.product(bot_names, bot_names):
        if name_x == name_o:
            continue
        BotX = BOT_CLASSES[name_x]
        BotO = BOT_CLASSES[name_o]
        x_wins = o_wins = draws = 0
        for _ in range(games_per_pair):
            game_seed = rng.randint(0, 10**6)
            bot_x = BotX()
            bot_o = BotO()
            result = play_game(bot_x, bot_o, seed=game_seed)
            if result == "X":
                x_wins += 1
            elif result == "O":
                o_wins += 1
            else:
                draws += 1
        results.append(
            {
                "X_bot": name_x,
                "O_bot": name_o,
                "games": games_per_pair,
                "X_wins": x_wins,
                "O_wins": o_wins,
                "draws": draws,
            }
        )

    # Save CSV
    out_path = Path(output_csv)
    with out_path.open("w", newline="") as f:
        writer = csv.DictWriter(
            f, fieldnames=["X_bot", "O_bot", "games", "X_wins", "O_wins", "draws"]
        )
        writer.writeheader()
        writer.writerows(results)
    print(f"Saved results to {out_path.resolve()}")


if __name__ == "__main__":
    run_tournament()
