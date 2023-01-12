# Config object
__author__ = "Matteo Golin"

# Imports
import json
from dataclasses import dataclass
from typing import Self

# Constants


# Classes
@dataclass()
class Animation:
    frame_duration: int
    scale: int
    colours: tuple[str, str]  # Dead, alive


@dataclass
class Config:

    dimensions: tuple[int, int]
    epochs: int
    animation: Animation

    @classmethod
    def from_json_file(cls, filepath: str) -> Self:

        """Returns config file data as dictionary object."""

        with open(filepath, 'r') as config:
            data = json.load(config)

        # Unpack data
        dimensions = data["dimensions"]
        animation = data["animation"]
        colours = animation["colours"]
        epochs = data["epochs"]

        dimensions = (
            dimensions["columns"],
            dimensions["rows"]
        )

        animation = Animation(
            animation["frame_duration"],
            animation["scale"],
            (
                colours["dead"],
                colours["alive"]
            )
        )

        return Config(
            epochs=epochs,
            dimensions=dimensions,
            animation=animation
        )
