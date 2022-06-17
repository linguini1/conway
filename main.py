# Conway's game of life
__author__ = "Matteo Golin"

# Imports
# Structural classes
from classes.grid import Grid
from classes.gif import GIFExporter
from classes.config import Config
from utils import export_seed, previous_seed

# Cells
from classes.cells.maze import MazeCell
from classes.cells.classic import ClassicCell

# Seeds
from classes.seeds.chaos import ChaosSeed
from classes.seeds.glider import GliderSeed


# Main
def main():

    # Start parameters
    config = Config()
    seed = ChaosSeed(
        cell_number=int(
            0.3  # Percentage of map to cover
            * config.dimensions[0]
            * config.dimensions[1]
        ),
        deviation=8
    ).translate((40, 40))
    export_seed(seed)  # Export seed

    # Create game
    grid = Grid(
        dimensions=config.dimensions,
        seed=seed,
        epochs=config.epochs,
        cell_type=ClassicCell,
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
