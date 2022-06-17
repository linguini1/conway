# Utility functions
__author__ = "Matteo Golin"

# Imports
from customtypes import Coordinates
import json

# Constants
SEED_FILE_NAME = "previous_seed.json"


# Functions
def add_vector(coords: Coordinates, vector: Coordinates) -> Coordinates:

    """Returns the result of adding a vector to a coordinate pair."""

    x, y = coords
    X, Y = vector

    return x + X, y + Y


def export_seed(seed: list[Coordinates]) -> None:

    """Exports the previously used seed in JSON format."""

    with open(SEED_FILE_NAME, 'w') as file:
        json.dump(seed, file)


def previous_seed() -> list[Coordinates]:

    """Returns the previously used seed from the file."""

    with open(SEED_FILE_NAME, 'r') as file:
        data = json.load(file)

    return [tuple(coordinate) for coordinate in data]
