# Seed base class
__author__ = "Matteo Golin"

# Imports
from customtypes import Coordinates
from utils import add_vector


# Class
class Seed:

    """Base interface for seed class. Implements cartesian coordinate system."""

    def __init__(self) -> None:
        self.coordinates: list[Coordinates] = []

    def translate(self, new_center: Coordinates) -> list[Coordinates]:

        """
        Returns the coordinates defining the seed translated so that the center
        matches the passed center coordinate.
        """

        return [add_vector(coord, new_center) for coord in self.coordinates]

    def __repr__(self):
        return self.coordinates
