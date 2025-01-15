# Oscillating seed classes
__author__ = "Matteo Golin"

# Imports
from classes.seeds.seed import Seed


# Classes
class PulsarSeed(Seed):

    """Pulsar oscillator from the classic CGOL."""

    def __init__(self):
        super().__init__("Pulsar", wiki_link="https://conwaylife.com/wiki/Pulsar")

        self.coordinates = [
            (-2, 0), (-3, 0), (-4, 0),
            (2, 0), (3, 0), (4, 0),
            (0, 1), (0, 2), (0, 3),
            (0, -1), (0, -2), (0, -3)
        ]


class BlinkerSeed(Seed):

    """Blinker oscillator from the classic CGOL."""

    def __init__(self):
        super().__init__("Blinker", wiki_link="https://conwaylife.com/wiki/Blinker")

        self.coordinates = [
            (-1, 0), (0, 0), (1, 0)
        ]


class ToadSeed(Seed):

    """Toad oscillator from the classic CGOL."""

    def __init__(self):
        super().__init__("Toad", wiki_link="https://conwaylife.com/wiki/Toad")

        self.coordinates = [
            (-1, 0), (0, 0), (1, 0),
            (0, 1), (1, 1), (2, 1)
        ]


class BeaconSeed(Seed):

    """Beacon oscillator from the classic CGOL."""

    def __init__(self):
        super().__init__("Beacon", wiki_link="https://conwaylife.com/wiki/Beacon")

        self.coordinates = [
            (0, 0), (0, 1), (-1, 0), (-1, 1),
            (1, -1), (2, -1), (1, -2), (2, -2)
        ]


class PentaDecathlonSeed(Seed):

    """Pentadecathlon oscillator from the classic CGOL."""

    def __init__(self):
        super().__init__("Pentadecathlon", wiki_link="https://conwaylife.com/wiki/Pentadecathlon")

        self.coordinates = [
            (-4, 0), (-3, 0), (-2, 1), (-2, -1), (-1, 0), (0, 0),
            (1, 0), (2, 0), (3, 1), (3, -1), (4, 0), (5, 0)
        ]
