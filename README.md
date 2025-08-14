
# Tic-Tac-Toe AI

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen)
![Coverage](https://img.shields.io/badge/coverage-pytest--cov-green)

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/3/32/Tic_tac_toe.svg" width="120" alt="Tic-Tac-Toe">
</p>

## Overview

**Tic-Tac-Toe AI** is a Python project featuring a modular engine, multiple AI strategies (random, rules-based, minimax), and a CLI for human and bot tournaments. Designed for extensibility, testing, and learning AI techniques.

## Features
- Pure-Python board engine
- Multiple AI bots: Random, Rules, Minimax
- CLI for human vs bot and bot vs bot matches
- Tournament runner and results
- Jupyter notebook for analysis
- Full test suite with coverage
- Pre-commit hooks for code quality

## Installation

```bash
git clone https://github.com/brainthra/tic-tac-toe.git
cd tic-tac-toe
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
pre-commit install
```

## Usage

### Play (CLI)

Human vs Random:
```bash
python -m cli.main --x human --o random
```
Random vs Random:
```bash
python -m cli.main --x random --o random --seed 42
```

### Tournament
```bash
python -m cli.tournament --x minimax --o rules --games 100
```

## AI Bots
- **RandomBot**: Plays random legal moves
- **RulesBot**: Uses simple heuristics
- **MinimaxBot**: Optimal play using minimax algorithm

## Testing

Run all tests and check coverage:
```bash
pytest
```

## Notebooks

See [`notebooks/tournament.ipynb`](notebooks/tournament.ipynb) for analysis and bot comparison.


## License

MIT License. See [LICENSE](LICENSE).
