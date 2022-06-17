# Maze cell class
__author__ = "Matteo Golin"

# Imports
from .basecell import Cell


# Class
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
