# Custom types
__author__ = "Matteo Golin"

# Imports
from classes.cell import Cell

# Types
GridDimension = tuple[int, int]
Coordinates = tuple[int, int]
GridField = list[list[Cell]]

Seed = list[Coordinates]
