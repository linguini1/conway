# Static seed classes
__author__ = "Matteo Golin"

# Imports
from classes.seeds.seed import Seed


# Classes
class SquareSeed(Seed):

    """Square, static shape."""

    def __init__(self):
        super().__init__()

        self.coordinates = [
            (0, 0), (0, 1),
            (1, 0), (1, 1)
        ]


class BeehiveSeed(Seed):

    """Beehive shape from origin COGL."""

    def __init__(self):
        super().__init__()

        self.coordinates = [
            (-1, 0), (0, 1), (1, 1),
            (0, -1), (1, -1), (2, 0)
        ]


class LoafSeed(Seed):
    """Loaf shape from origin COGL."""

    def __init__(self):
        super().__init__()

        self.coordinates = [
            (0, 0), (-1, 1), (1, -1),
            (0, 2), (1, 2), (2, 1), (2, 0)
        ]
