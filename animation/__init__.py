# Creates an animation from the game
__author__ = "Matteo Golin"

# Imports
from PIL import Image, ImageColor
from classes.grid import Grid
from customtypes import GridField

# CONSTANTS
DEFAULT_ALIVE = ImageColor.getrgb("#222323")
DEFAULT_DEAD = ImageColor.getrgb("#f0f6f0")
FILENAME = "animation.gif"


# Class
class GIFExporter:

    def __init__(self, grid: Grid, epochs: int, scale: int = 10):
        self.grid = grid
        self.size = grid.columns, grid.rows
        self.epochs = epochs
        self.scale = scale
        self.frames = []

    def __create_image(self, snapshot: GridField) -> Image:

        """Returns an image based on the passed grid snapshot."""

        image = Image.new('RGB', self.size)

        for y in range(self.grid.rows):
            for x in range(self.grid.columns):
                current_cell = snapshot[y][x]

                # Decide on colour
                if current_cell.alive:
                    colour = DEFAULT_ALIVE
                else:
                    colour = DEFAULT_DEAD

                image.putpixel((x, y), colour)  # Place colour on image

        # Resize image
        new_size = self.size[0] * self.scale, self.size[1] * self.scale
        image = image.resize(new_size, Image.NEAREST)

        return image

    def __create_frames(self):

        """Creates images from grid values and stores them as frames."""

        for _ in range(self.epochs):
            snapshot = self.grid.next_generation()
            self.frames.append(self.__create_image(snapshot))

    def export(self):

        """Exports a GIF file of the game."""

        self.__create_frames()  # Create the frames

        gif = self.frames[0]  # Grab the first image as the base
        gif.save(
            fp=FILENAME,
            format='GIF',
            append_images=self.frames,
            save_all=True,
            duration=200,
            loop=0
        )
