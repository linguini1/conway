# Oscillating seed classes
__author__ = "Matteo Golin"

# Imports
from classes.seeds.seed import Seed


# Classes
class PulsarSeed(Seed):

    """Radiation-symbol looking seed."""

    def __init__(self):
        super().__init__()

        self.coordinates = [
            (-2, 0), (-3, 0), (-4, 0),
            (2, 0), (3, 0), (4, 0),
            (0, 1), (0, 2), (0, 3),
            (0, -1), (0, -2), (0, -3)
        ]
