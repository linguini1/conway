# Seed classes
__author__ = "Matteo Golin"

# Imports
from customtypes import Coordinates
from .seed import Seed
import random


# Class
class ChaosSeed(Seed):

    """Seed that is randomly generated."""

    def __init__(self, cell_number: int, deviation: int = 3) -> None:
        super().__init__()

        # Make random coordinates
        self.coordinates = []
        for _ in range(cell_number):

            x = int(random.gauss(0, deviation))
            y = int(random.gauss(0, deviation))

            self.coordinates.append((x, y))


class MoreChaoticSeed(Seed):

    def __init__(self, cell_number: int, dimensions: Coordinates) -> None:
        super().__init__()

        # Unpack dimensions
        columns, rows = dimensions

        # Make random coordinates
        self.coordinates = []
        for _ in range(cell_number):
            y = random.randint(0, rows - 1)
            x = random.randint(0, columns - 1)

            self.coordinates.append((x, y))
