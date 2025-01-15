# Static seed classes
__author__ = "Matteo Golin"

# Imports
from classes.seeds.seed import Seed


# Classes
class SquareSeed(Seed):

    """Square, static shape."""

    def __init__(self):
        super().__init__("Square Seed")

        self.coordinates = [
            (0, 0), (0, 1),
            (1, 0), (1, 1)
        ]


class BeehiveSeed(Seed):

    """Beehive shape from origin CGOL."""

    def __init__(self):
        super().__init__("Beehive", wiki_link="https://conwaylife.com/wiki/Beehive")

        self.coordinates = [
            (-1, 0), (0, 1), (1, 1),
            (0, -1), (1, -1), (2, 0)
        ]


class LoafSeed(Seed):

    """Loaf shape from origin CGOL."""

    def __init__(self):
        super().__init__("Loaf", wiki_link="https://conwaylife.com/wiki/Loaf")

        self.coordinates = [
            (0, 0), (-1, 1), (1, -1),
            (0, 2), (1, 2), (2, 1), (2, 0)
        ]


class BoatSeed(Seed):

    """Boat shape from origin CGOL."""

    def __init__(self):
        super().__init__("Boat", wiki_link="https://conwaylife.com/wiki/Boat")

        self.coordinates = [
            (-1, 0), (1, 0), (-1, 1), (0, 1), (0, -1)
        ]


class TubSeed(Seed):

    """Tub shape from origin CGOL."""

    def __init__(self):
        super().__init__("Tub", wiki_link="https://conwaylife.com/wiki/Tub")

        self.coordinates = [
            (-1, 0), (1, 0), (0, -1), (0, 1)
        ]
