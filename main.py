# Conway's game of life
__author__ = "Matteo Golin"

# Imports
# Structural classes
from classes.grid import Grid
from classes.gif import GIFExporter
from classes.image import ImageExporter
from classes.config import Config
from utils import export_seed, previous_seed, map_center, percentage_of_map

# Cells
from classes.cells import MazeCell, ClassicCell

# Seeds
from classes.seeds import MoreChaoticSeed
from classes.seeds import ChaosSeed


# Main
def main():

    # Start parameters
    config = Config()

    seed = ChaosSeed(
        cell_number=20,
        deviation=4
    ).translate(map_center(config.dimensions))
    #seed = previous_seed()
    export_seed(seed)  # Export seed

    # Create game
    grid = Grid(
        dimensions=config.dimensions,
        seed=seed,
        epochs=config.epochs,
        cell_type=MazeCell,
        continuous=True
    )

    # Export gif
    GIFExporter(
        grid=grid,
        scale=config.animation.scale,
        frame_duration=config.animation.duration,
    ).export(config.animation.colours)

    # Export images
    # ImageExporter(
    #     grid=grid,
    #     scale=config.animation.scale,
    #     step_size=1,
    # ).export(config.animation.colours)


if __name__ == '__main__':
    main()
