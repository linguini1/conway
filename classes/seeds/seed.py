# Seed base class
__author__ = "Matteo Golin"

# Imports
from customtypes import Coordinates
from typing import Self, Optional
from utils import add_vector


# Class
class Seed:

    """Base interface for seed class. Implements cartesian coordinate system."""

    def __init__(self, name: str, wiki_link: Optional[str] = None) -> None:
        self.coordinates: list[Coordinates] = []
        self.name: str = name
        self.wiki_link: Optional[str] = None

    def translate(self, new_center: Coordinates) -> None:

        """
        Translates the current seed somewhere else.
        """

        for i in range(len(self.coordinates)):
            self.coordinates[i] = add_vector(self.coordinates[i], new_center)

    @classmethod
    def from_plaintext(cls, filename: str) -> Self:
        """Load CGOL Wiki plain-text files describing a seed."""
        with open(filename, "r") as file:
            name = file.readline().replace("!","").replace(".cells","").strip()
            file.readline() # Skip author
            link = file.readline().replace("!", "").strip() # Wiki link
            file.readline() # Skip file link

            seed = cls(name, wiki_link=link)

            # Determine coordinates of starter cells

            for y, line in enumerate(file):
                for x, character in enumerate(line):
                    if character == "O":
                        seed.coordinates.append((x, y))

        return seed

    def __str__(self) -> str:
        if self.wiki_link is not None:
            return f"Seed({self.name}, link={self.wiki_link})"
        else:
            return f"Seed({self.name})"
