# Conway's game of life
__author__ = "Matteo Golin"

# Imports
from classes.grid import Grid
from animation import GIFExporter

# Constants
EPOCHS = 60


# Main
def main():

    dimensions = 20, 20
    seed = [
        (10, 6), (10, 7), (10, 8), (10, 12), (10, 13), (10, 14),
        (9, 10), (8, 10), (7, 10), (11, 10), (12, 10), (13, 10)
    ]

    grid = Grid(dimensions, seed=seed)
    exporter = GIFExporter(grid, EPOCHS)
    exporter.export()


if __name__ == '__main__':
    main()
