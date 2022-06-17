# Config object
__author__ = "Matteo Golin"

# Imports
import json
from dataclasses import dataclass

# Constants
FILE_NAME = "config.json"


# Classes
class Config:

    def __init__(self):

        data = self.__load_from_file()  # Load data

        # Unpack data
        dimensions = data["dimensions"]
        animation = data["animation"]
        colours = animation["colours"]

        self.epochs = data["epochs"]

        self.dimensions = (
            dimensions["columns"],
            dimensions["rows"]
        )

        self.animation = Animation(
            animation["duration"],
            animation["scale"],
            (
                colours["dead"],
                colours["alive"]
            )
        )

    @staticmethod
    def __load_from_file() -> dict:

        """Returns config file data as dictionary object."""

        with open(FILE_NAME, 'r') as config:
            data = json.load(config)

        return data


@dataclass()
class Animation:
    duration: int
    scale: int
    colours: tuple[str, str]  # Dead, alive
