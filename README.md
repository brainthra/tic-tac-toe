# Tic-Tac-Toe AI

## Core Engine

This commit contains:
- `engine/board.py`: A pure-Python Tic-Tac-Toe board class with:
  - State representation
  - Move legality checking
  - Win/draw detection
  - Player switching
- `tests/test_board.py`: Pytest unit tests for engine correctness.

Run tests:
```bash
pip install -r requirements.txt
pytest
```

## Play (CLI)

Human vs Random:
```bash
python -m cli.main --x human --o random
```
Random vs Random:
```bash
python -m cli.main --x random --o random --seed 42
```
