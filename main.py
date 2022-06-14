# Conway's game of life
__author__ = "Matteo Golin"

# Imports
from classes.grid import Grid
from classes.gif import GIFExporter

# Constants
EPOCHS = 150


# Main
def main():

    # Start parameters
    dimensions = 20, 20
    seed = [
        (10, 6), (10, 7), (10, 8), (10, 12), (10, 13), (10, 14),
        (9, 10), (8, 10), (7, 10), (11, 10), (12, 10), (13, 10)
    ]

    # Create game
    grid = Grid(
        dimensions=dimensions,
        seed=seed,
        epochs=EPOCHS
    )

    # Export gif
    GIFExporter(
        grid=grid,
        scale=20,  # 20x the grid size,
        show_progress=True,
    ).export()


if __name__ == '__main__':
    main()
