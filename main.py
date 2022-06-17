# Conway's game of life
__author__ = "Matteo Golin"

# Imports
from classes.grid import Grid
from classes.gif import GIFExporter
from classes.config import Config
from classes.cells.maze import MazeCell
from classes.seeds.chaos import ChaosSeed

# Main
def main():

    # Start parameters
    config = Config()
    seed = ChaosSeed(config.dimensions).translate((25, 25))

    # Create game
    grid = Grid(
        dimensions=config.dimensions,
        seed=seed,
        epochs=config.epochs,
        cell_type=MazeCell,
    )

    # Export gif
    GIFExporter(
        grid=grid,
        scale=config.animation.scale,
        frame_duration=config.animation.duration,
        show_progress=True,
    ).export(config.animation.colours)


if __name__ == '__main__':
    main()
