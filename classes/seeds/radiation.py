# Radiation seed class
__author__ = "Matteo Golin"

# Imports
from .seed import Seed


# Class
class RadiationSeed(Seed):

    """Radiation-symbol looking seed."""

    def __init__(self):
        super().__init__()

        self.coordinates = [
            (-2, 0), (-3, 0), (-4, 0),
            (2, 0), (3, 0), (4, 0),
            (0, 1), (0, 2), (0, 3),
            (0, -1), (0, -2), (0, -3)
        ]
