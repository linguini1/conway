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


def export_seed(seed: list[Coordinates]) -> None:

    """Exports the previously used seed in JSON format."""

    with open(SEED_FILE_NAME, 'w') as file:
        json.dump(seed, file)


def previous_seed() -> list[Coordinates]:

    """Returns the previously used seed from the file."""

    with open(SEED_FILE_NAME, 'r') as file:
        data = json.load(file)

    return [tuple(coordinate) for coordinate in data]


def map_center(dimensions: Coordinates) -> Coordinates:

    """Returns the (approximate) center of the map from its dimensions as x, y coordinates."""

    x, y = dimensions

    return round(x / 2), round(y / 2)


def percentage_of_map(percentage: float, dimensions: Coordinates) -> int:

    assert 0 < percentage <= 100, "Percentage must be greater than 0, up to 100."

    y, x = dimensions

    """Returns the number of points required to cover the passed percentage of the map dimensions."""

    return round((percentage / 100) * x * y)
