# Utility functions
__author__ = "Matteo Golin"

# Imports
from customtypes import Coordinates
import json

# Constants
SEED_FILE_NAME = "previous_seed.json"


# Functions
def add_vector(point1: Coordinates, point2: Coordinates) -> Coordinates:

    """Returns the result of adding two points."""

    x1, y1 = point1
    x2, y2 = point2

    return x1 + x2, y1 + y2

def map_center(dimensions: tuple[int, int]) -> Coordinates:

    """Returns the (approximate) center of the map from its dimensions as x, y coordinates."""

    x, y = dimensions

    return round(x / 2), round(y / 2)


def percentage_of_map(percentage: float, dimensions: tuple[int, int]) -> int:

    """
    Returns the number of cells required to cover the passed percentage of the map dimensions. Percentages should be
    between 0 and 100.
    """

    assert 0 < percentage <= 100, "Percentage must be greater than 0, up to 100."

    y, x = dimensions

    return round((percentage / 100) * x * y)
