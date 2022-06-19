# Oscillating seed classes
__author__ = "Matteo Golin"

# Imports
from classes.seeds.seed import Seed


# Classes
class PulsarSeed(Seed):

    """Pulsar oscillator from the classic COGL."""

    def __init__(self):
        super().__init__()

        self.coordinates = [
            (-2, 0), (-3, 0), (-4, 0),
            (2, 0), (3, 0), (4, 0),
            (0, 1), (0, 2), (0, 3),
            (0, -1), (0, -2), (0, -3)
        ]


class PulsarPredecessorSeed(Seed):

    """Develops into pulsar."""

    def __init__(self) -> None:
        super().__init__()

        self.coordinates = [
            (0, -2), (0, -1), (0, 0), (0, 1), (0, 2),
            (1, -2), (1, 2)
        ]
