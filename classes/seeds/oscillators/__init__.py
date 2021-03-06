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
            (-1, 0), (0, 0), (1, 0)
        ]


class ToadSeed(Seed):

    """Toad oscillator from the classic COGL."""

    def __init__(self):
        super().__init__()

        self.coordinates = [
            (-1, 0), (0, 0), (1, 0),
            (0, 1), (1, 1), (2, 1)
        ]


class BeaconSeed(Seed):

    """Beacon oscillator from the classic COGL."""

    def __init__(self):
        super().__init__()

        self.coordinates = [
            (0, 0), (0, 1), (-1, 0), (-1, 1),
            (1, -1), (2, -1), (1, -2), (2, -2)
        ]


class PentaDecathlonSeed(Seed):

    """Penta-decathlon oscillator from the classic COGL."""

    def __init__(self):
        super().__init__()

        self.coordinates = [
            (-4, 0), (-3, 0), (-2, 1), (-2, -1), (-1, 0), (0, 0),
            (1, 0), (2, 0), (3, 1), (3, -1), (4, 0), (5, 0)
        ]
