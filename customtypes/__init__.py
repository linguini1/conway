# Custom types
__author__ = "Matteo Golin"

# Imports
from typing import Generator
from classes.cells.basecell import Cell

# Types
GridDimension = tuple[int, int]
Coordinates = tuple[int, int]
GridField = list[list[Cell]]
Game = Generator[GridField]

Seed = list[Coordinates]
