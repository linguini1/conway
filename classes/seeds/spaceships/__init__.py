# Spaceship seeds
__author__ = "Matteo Golin"

# Imports
from classes.seeds.seed import Seed


# Classes
class GliderSeed(Seed):
    
    """Basic glider object from the classic version of Conway's game of life."""

    def __init__(self):
        super().__init__()

        self.coordinates = [
            (0, 1),
            (1, 0),
            (-1, -1),
            (-1, 0),
            (-1, 1),
        ]
