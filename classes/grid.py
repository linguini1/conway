# Grid class
__author__ = "Matteo Golin"

# Imports
from customtypes import GridDimension, Coordinates, GridField, Game, Cell
from classes.cells.classic import ClassicCell
from utils import add_vector
import pprint

# Constants
NEIGHBOUR_VECTORS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 1),  # Center cell does not count
    (1, -1), (1, 0), (1, 1),
]


# Class
class Grid:

    """Grid that hosts the cells."""

    def __init__(
            self,
            dimensions: GridDimension,
            epochs: int,
            seed: list[Coordinates] = None,
            cell_type: Cell = ClassicCell,
            continuous: bool = False,
    ):
        self.columns, self.rows = dimensions
        self.seed = seed
        self.epochs = epochs
        self.cell_type = cell_type
        self.continuous = continuous
        self.array = self.__initialize_array()

    def __initialize_array(self) -> GridField:

        """Sets up the array representation of the grid using the seed."""

        # Creates the default array
        array = [[self.cell_type() for _ in range(self.columns)] for _ in range(self.rows)]

        # Add seed
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

                # Python negative indexes should not be used here
                if x < 0 or y < 0:
                    pass

                # Valid, non-negative index
                else:
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

        return self.array.copy()

    def create_game(self) -> Game:

        """Returns a generator containing all generations (epochs) of the game."""

        # Continues until game becomes static
        if self.continuous:

            previous: list[list[list[bool]]] = []
            while True:
                current = self.next_generation()
                current_bool = [[cell.alive for cell in row] for row in current]

                if current_bool in previous:
                    break

                if len(previous) < 18:
                    previous.append(current_bool)
                else:
                    previous.append(current_bool)
                    previous.pop(0)

                yield current

        else:
            for _ in range(self.epochs):
                yield self.next_generation()

    def __equal_generations(self, gen1: list[list[bool]], gen2: list[list[bool]]) -> bool:

        """Returns true if two generations are exactly the same."""

        # Base case
        if gen1 is None or gen2 is None:
            return False

        for _ in range(self.rows):

            if gen1[_] != gen2[_]:
                return False

        return True  # If all rows are equal, return true

    def __repr__(self):

        representation = ""

        for row in self.array:
            for cell in row:
                representation += f"{str(cell):>3}"
            representation += "\n"

        return representation
