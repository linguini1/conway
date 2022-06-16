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
        self.epochs = data["epochs"]

    @staticmethod
    def __load_from_file() -> dict:

        """Returns config file data as dictionary object."""

        with open(FILE_NAME, 'r') as config:
            data = json.load(config)

        return data


@dataclass()
class Dimensions:
    rows: int
    columns: int


@dataclass()
class Colours:
    dead: str
    alive: str


@dataclass()
class Animation:
    duration: int
    colours: Colours
