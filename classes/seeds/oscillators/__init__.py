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


class BlinkerSeed(Seed):

    """Blinker oscillator from the classic COGL."""

    def __init__(self):
        super().__init__()

        self.coordinates = [
            (-1, 0), (0, 0), (0, 1)
        ]


class ToadSeed(Seed):

    """Toad oscillator from the classic COGL."""

    def __init__(self):
        super().__init__()

        self.coordinates = [
            (-1, 0), (0, 0), (1, 0),
            (0, 1), (1, 1), (2, 1)
        ]
