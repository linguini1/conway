# Utility functions
__author__ = "Matteo Golin"

# Imports
from customtypes import Coordinates


# Functions
def add_vector(coords: Coordinates, vector: Coordinates) -> Coordinates:

    """Returns the result of adding a vector to a coordinate pair."""

    x, y = coords
    X, Y = vector

    return x + X, y + Y