# Static seed classes
__author__ = "Matteo Golin"

# Imports
from classes.seeds.seed import Seed


# Classes
class SquareSeed(Seed):

    """Radiation-symbol looking seed."""

    def __init__(self):
        super().__init__()

        self.coordinates = [
            (0, 0), (0, 1),
            (1, 0), (1, 1)
        ]
