# Conway's game of life
__author__ = "Matteo Golin"

# Imports
from classes.grid import Grid
from classes.config import Config
from classes.exporters import ImageExporter, GIFExporter
from utils import map_center

# Cells
from classes.cells import MazeCell, ClassicCell, FrostCell

# Seeds
from classes.seeds import Seed

# Constants
CONFIG_FILE = "config.json"


# Main
def main():

    # Start parameters
    config = Config.from_json_file(CONFIG_FILE)

    seed = Seed.from_plaintext( "./seeds/simkinsp60.cells")
    seed.translate(map_center(config.dimensions))
    print(seed)

    # Create game
    print("Starting grid generation...")
    grid = Grid(
        cell_type=ClassicCell,
        dimensions=config.dimensions,
        seed=seed,
        epochs=config.epochs,
    )
    print("Grid generation complete.\n")

    # Export gif
    gif_exporter = GIFExporter(
        grid=grid,
        scale=config.animation.scale,
        frame_duration=config.animation.frame_duration,
    )
    gif_exporter.export(filepath="./animation", colours=config.animation.colours)

    # Export images
    # image_exporter = ImageExporter(
    #     grid=grid,
    #     scale=config.animation.scale,
    #     step_size=20,
    # )
    # image_exporter.extension = "jpeg"
    # image_exporter.export(filepath="./image", colours=config.animation.colours)


if __name__ == '__main__':
    main()
