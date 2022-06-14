# Creates an animation from the game
__author__ = "Matteo Golin"

# Imports
from PIL import Image, ImageColor
from classes.grid import Game
from customtypes import GridField

# CONSTANTS
DEFAULT_ALIVE = ImageColor.getrgb("#222323")
DEFAULT_DEAD = ImageColor.getrgb("#f0f6f0")
FILENAME = "animation.gif"


# Class
class GIFExporter:

    def __init__(self, game: Game, size: tuple[int, int], scale: int = 10):
        self.game = game
        self.scale = scale
        self.size = size

        # Storing frames
        self.frames = []

    def __create_image(self, snapshot: GridField) -> Image:

        """Returns an image based on the passed grid snapshot."""

        image = Image.new('RGB', self.size)

        for y in range(self.size[1]):  # Rows
            for x in range(self.size[0]):  # Columns
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

        for frame in self.game:
            image = self.__create_image(frame)
            self.frames.append(image)

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
