# Default cell class
__author__ = "Matteo Golin"

# Imports
from .cell import Cell


# Class
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
