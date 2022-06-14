# Cell base class
__author__ = "Matteo Golin"

# Imports
from abc import ABC, abstractmethod


# Class
class Cell(ABC):

    """Base cell class for all cells to inherit from."""

    def __init__(self, alive: bool = False):
        self.alive = alive
        self.next_state = alive

    @abstractmethod
    def evaluate_state(self, neighbours: int):
        """Evaluates the cell's next state and stores it."""
        ...

    def advance_state(self):
        """Cell takes on its stored next state."""
        self.alive = self.next_state

    def __repr__(self):

        # Grid cell displays full
        if self.alive:
            return "#"

        # Grid cell displays empty
        else:
            return "."
