# Default cell class
__author__ = "Matteo Golin"

# Imports
from .basecell import Cell


# Class
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
            