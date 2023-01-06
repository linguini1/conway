# Custom types
__author__ = "Matteo Golin"

# Imports
from typing import Generator
from classes.cells import Cell

# Types
GridDimension = tuple[int, int]
Coordinates = tuple[int, int]
GridField = list[list[Cell]]
Game = Generator
