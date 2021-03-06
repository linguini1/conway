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


class LightSpaceshipSeed(Seed):

    """Light-weight spaceship from original COGL."""

    def __init__(self):
        super().__init__()

        self.coordinates = [
            (-1, 1), (-2, 0), (-2, -1), (-2, -2), (-1, -2), (0, -2),
            (1, -2), (2, -1), (2, 1)
        ]


class MiddleSpaceshipSeed(Seed):

    """Light-weight spaceship from original COGL."""

    def __init__(self):
        super().__init__()

        self.coordinates = [
            (-1, 1), (0, 1), (1, 1),
            (-2, 0), (-1, 0), (0, 0), (1, 0), (2, 0),
            (-2, -1), (-1, -1), (0, -1), (2, -1), (3, -1),
            (1, -2), (2, -2)
        ]


class HeavySpaceshipSeed(Seed):

    """Light-weight spaceship from original COGL."""

    def __init__(self):
        super().__init__()

        self.coordinates = [
            (-2, 1), (-1, 1), (0, 1), (1, 1),
            (-3, 0), (-2, 0), (-1, 0), (0, 0), (1, 0), (2, 0),
            (-3, -1), (-2, -1), (-1, -1), (0, -1), (2, -1), (3, -1),
            (1, -2), (2, -2)
        ]
