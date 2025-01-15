# Spaceship seeds
__author__ = "Matteo Golin"

# Imports
from classes.seeds.seed import Seed


# Classes
class GliderSeed(Seed):
    
    """Basic glider object from the classic version of Conway's game of life."""

    def __init__(self):
        super().__init__("Glider", wiki_link="https://conwaylife.com/wiki/Glider")

        self.coordinates = [
            (0, 1),
            (1, 0),
            (-1, -1),
            (-1, 0),
            (-1, 1),
        ]


class LightSpaceshipSeed(Seed):

    """Light-weight spaceship from original CGOL."""

    def __init__(self):
        super().__init__("Lightweight Spaceship", wiki_link="https://conwaylife.com/wiki/Lightweight_spaceship")

        self.coordinates = [
            (-1, 1), (-2, 0), (-2, -1), (-2, -2), (-1, -2), (0, -2),
            (1, -2), (2, -1), (2, 1)
        ]


class MiddleSpaceshipSeed(Seed):

    """Light-weight spaceship from original CGOL."""

    def __init__(self):
        super().__init__("Middleweight Spaceship", wiki_link="https://conwaylife.com/wiki/Middleweight_spaceship")

        self.coordinates = [
            (-1, 1), (0, 1), (1, 1),
            (-2, 0), (-1, 0), (0, 0), (1, 0), (2, 0),
            (-2, -1), (-1, -1), (0, -1), (2, -1), (3, -1),
            (1, -2), (2, -2)
        ]


class HeavySpaceshipSeed(Seed):

    """Light-weight spaceship from original CGOL."""

    def __init__(self):
        super().__init__("Heavyweight Spaceship", wiki_link="https://conwaylife.com/wiki/Heavyweight_spaceship")

        self.coordinates = [
            (-2, 1), (-1, 1), (0, 1), (1, 1),
            (-3, 0), (-2, 0), (-1, 0), (0, 0), (1, 0), (2, 0),
            (-3, -1), (-2, -1), (-1, -1), (0, -1), (2, -1), (3, -1),
            (1, -2), (2, -2)
        ]
