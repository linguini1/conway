# Miscellaneous seed classes
__author__ = "Matteo Golin"

# Imports
from classes.seeds.seed import Seed


# Classes
class ShoeBoxSeed(Seed):

    """Shoebox looking seed from the community on r/gameoflife."""

    def __init__(self) -> None:
        super().__init__("Shoebox")

        self.coordinates = [
            (-1, -1), (0, -1), (1, -1), (2, -1),
            (-1, 0), (2, 0),
            (-1, 1), (1, 1), (2, 1)
        ]


class PulsarPredecessorSeed(Seed):

    """Develops into pulsar."""

    def __init__(self) -> None:
        super().__init__("Pulsar Predecessor")

        self.coordinates = [
            (0, -2), (0, -1), (0, 0), (0, 1), (0, 2),
            (1, -2), (1, 2)
        ]
