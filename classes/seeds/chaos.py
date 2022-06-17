# Random seed class
__author__ = "Matteo Golin"

# Imports
from customtypes import Coordinates
from .seed import Seed
import random

# Class
class ChaosSeed(Seed):

    """Seed that is randomly generated."""

    def __init__(self, grid_dimensions: Coordinates)  -> None:
        super().__init__()

        # Unpack dimensions to determine seed coords
        columns, rows = grid_dimensions
        half_cols = columns / 2
        half_rows = rows / 2

        # Make random coords
        self.coords = []
        for _ in range(20):
            x = random.randint(
                -(half_cols),
                (half_cols)
            )

            y = random.randint(
                -(half_rows),
                (half_rows)
            )

            self.coords.append((x, y))