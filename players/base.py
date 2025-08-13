# players/base.py
from abc import ABC, abstractmethod
from typing import Protocol
from engine.board import Board

class Player(ABC):
    """Abstract player interface."""

    @abstractmethod
    def choose_move(self, board: Board) -> int:
        """Return a legal move index [0..8] for the given board."""
        raise NotImplementedError

class HumanIO(Protocol):
    """Protocol for human I/O; lets us mock/replace input/output if needed."""
    def read_move(self, prompt: str) -> str: ...
    def write(self, text: str) -> None: ...
