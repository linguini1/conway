# Grid class
__author__ = "Matteo Golin"

# Imports
from customtypes import GridDimension, Coordinates, GridField, Game, Cell
from classes.cells.classic import ClassicCell
from utils import add_vector

# Constants
NEIGHBOUR_VECTORS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 1),  # Center cell does not count
    (1, -1), (1, 0), (1, 1),
]


# Class
class Grid:

    """Grid that hosts the cells."""

    def __init__(self, dimensions: GridDimension, epochs: int, seed: list[Coordinates] = None, cell_type: Cell = ClassicCell):
        self.columns, self.rows = dimensions
        self.seed = seed
        self.epochs = epochs
        self.cell_type = cell_type
        self.array = self.__initialize_array()

    def __initialize_array(self) -> GridField:

        """Sets up the array representation of the grid using the seed."""

        # Creates the default array
        array = [[self.cell_type() for _ in range(self.columns)] for _ in range(self.rows)]

        # Add seed TODO
        for coord in self.seed:
            x, y = coord
            array[y][x] = self.cell_type(alive=True)

        return array

    def get_neighbours(self, index: Coordinates) -> int:

        """Returns the number of living neighbours in the 8 surrounding cells."""

        neighbours = 0

        for vector in NEIGHBOUR_VECTORS:
            x, y = add_vector(index, vector)

            try:
                current_neighbour = self.array[y][x]
                if current_neighbour.alive:
                    neighbours += 1
            except IndexError:
                pass  # Counts as dead cell

        return neighbours

    def next_generation(self) -> GridField:

        """Advances all cells in the grid to their next state and returns a snapshot of the grid field."""

        # Evaluate next state
        for y in range(self.rows):
            for x in range(self.columns):
                current_cell = self.array[y][x]
                neighbours = self.get_neighbours((x, y))
                current_cell.evaluate_state(neighbours)

        # Advance all states
        for y in range(self.rows):
            for x in range(self.columns):
                current_cell = self.array[y][x]
                current_cell.advance_state()

        return self.array

    def create_game(self) -> Game:

        """Returns a generator containing all generations (epochs) of the game."""

        for _ in range(self.epochs):
            yield self.next_generation()

    def __repr__(self):

        representation = ""

        for row in self.array:
            for cell in row:
                representation += f"{str(cell):>3}"
            representation += "\n"

        return representation
