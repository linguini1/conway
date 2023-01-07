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
from classes.cells import MazeCell, ClassicCell, FrostCell

# Seeds
from classes.seeds import MoreChaoticSeed
from classes.seeds import ChaosSeed
from classes.seeds.spaceships import MiddleSpaceshipSeed


# Main
def main():

    # Start parameters
    config = Config()

    seed = ChaosSeed(
        cell_number=percentage_of_map(10, config.dimensions),
        deviation=9
    ).translate(map_center(config.dimensions))

    # Seed import and export
    #seed = previous_seed()
    export_seed(seed)  # Export seed

    # Create game
    print("Starting grid generation...")
    grid = Grid(
        cell_type=FrostCell,
        dimensions=config.dimensions,
        seed=seed,
        epochs=config.epochs,
    )
    print("Grid generation complete.\n")

    # Export gif
    print("Running game...")
    GIFExporter(
        grid=grid,
        scale=config.animation.scale,
        frame_duration=config.animation.frame_duration,
    ).export(config.animation.colours)

    # Export images
    # ImageExporter(
    #     grid=grid,
    #     scale=config.animation.scale,
    #     step_size=100,
    # ).export(config.animation.colours)


if __name__ == '__main__':
    main()
