# Cell implementations
__author__ = "Matteo Golin"

# Imports
from abc import ABC, abstractmethod


# Classes
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


class ClassicCell(Cell):

    """Default implementation of the cell based on Conway's original game of life."""

    def __init__(self, alive: bool = False):
        super().__init__(alive)

    def evaluate_state(self, neighbours: int):

        # For a space that is populated
        if self.alive:

            # A cell with one or no neighbours dies
            if neighbours <= 1:
                self.next_state = False

            # A cell with four or more neighbours dies
            elif neighbours >= 4:
                self.next_state = False

            # A cell with two or three neighbours survives
            else:
                self.next_state = True

        # For a space that is unpopulated
        else:
            if neighbours == 3:
                self.next_state = True


class FrostCell(Cell):
    """
    B2345/S45678
    Named for its frost-like appearance during growth.
    """

    def __init__(self, alive: bool = False):
        super().__init__(alive)

    def evaluate_state(self, neighbours: int):

        # For space that is alive
        if self.alive:
            if neighbours >= 4:  # 4 or more neighbours to survive
                self.next_state = True
            else:
                self.next_state = False

        # For space that is dead
        else:
            if 2 <= neighbours <= 5:  # Born with between 2-5 neighbours
                self.next_state = True


class MazeCell(Cell):

    """
    B2345/S45678
    Named for its maze-like appearance during growth.
    """

    def __init__(self, alive: bool = False):
        super().__init__(alive)

    def evaluate_state(self, neighbours: int):

        # If already alive
        if self.alive:
            if 2 <= neighbours <= 5:  # 2-5 neighbours to survive
                self.next_state = True
            else:
                self.next_state = False

        # Dead
        else:
            if neighbours == 3:
                self.next_state = True

