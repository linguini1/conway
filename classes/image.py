# Creates an image from specific generations of the game
__author__ = "Matteo Golin"

# Imports
from PIL import Image, ImageColor
from classes.grid import Grid
from customtypes import GridField
from progress.bar import ChargingBar

# Constants
DEFAULT_COLOURS = "#222323", "#f0f6f0"
FILENAME = "image"


# Class
class ImageExporter:

    def __init__(self, grid: Grid, step_size: int, scale: int = 10):
        self.grid = grid
        self.size = grid.columns, grid.rows
        self.step_size = step_size
        self.scale = scale

    def __create_image(self, snapshot: GridField, colours: tuple[str, str]) -> Image:

        """Returns an image based on the passed grid snapshot."""

        # Unpack colours
        dead, alive = colours
        dead, alive = ImageColor.getrgb(dead), ImageColor.getrgb(alive)

        image = Image.new('RGB', self.size, dead)  # Define image

        for y in range(self.grid.rows):  # Rows
            for x in range(self.grid.columns):  # Columns
                current_cell = snapshot[y][x]

                # Decide on colour
                if current_cell.alive:
                    image.putpixel((x, y), alive)  # Place colour on image

        # Resize image
        new_size = self.size[0] * self.scale, self.size[1] * self.scale
        image = image.resize(new_size, Image.NEAREST)

        return image

    def __create_images(self, colours: tuple[str, str], progress_bar: ChargingBar, extension: str) -> None:

        """Creates all the images."""

        counter = 0
        for generation in self.grid.create_game():

            # Export image every step size
            if counter % self.step_size == 0:
                image = self.__create_image(generation, colours)
                image.save(f"./images/{FILENAME}_{counter // self.step_size}.{extension}")
                progress_bar.next()

            counter += 1

    def export(self, colours: tuple[str, str] = DEFAULT_COLOURS, png: bool = True) -> None:

        """Exports image files of the grid."""

        # Pick extension
        extension = "png" if png else "jpg"

        # Show progress
        if not self.grid.continuous:
            with ChargingBar("Creating images", max=(self.grid.epochs // self.step_size)) as bar:
                self.__create_images(colours, bar, extension)
