# Creates an animation from the game
__author__ = "Matteo Golin"

# Imports
from PIL import Image, ImageColor
from progress.bar import ChargingBar
from classes.grid import Grid
from customtypes import GridField

# CONSTANTS
DEFAULT_COLOURS = "#222323", "#f0f6f0"
FILENAME = "animation.gif"


# Class
class GIFExporter:

    def __init__(self, grid: Grid, scale: int = 10, frame_duration: int = 200, show_progress: bool = True):
        self.grid = grid
        self.size = grid.columns, grid.rows
        self.scale = scale
        self.frame_duration = frame_duration

        # Progress bar
        self.show_progress = show_progress

        # Storing frames
        self.frames = []

    def __create_image(self, snapshot: GridField, colours: tuple[str, str]) -> Image:

        """Returns an image based on the passed grid snapshot."""

        image = Image.new('RGB', self.size)
        
        # Unpack colours
        dead, alive = colours
        dead, alive = ImageColor.getrgb(dead), ImageColor.getrgb(alive)

        for y in range(self.grid.rows):  # Rows
            for x in range(self.grid.columns):  # Columns
                current_cell = snapshot[y][x]

                # Decide on colour
                if current_cell.alive:
                    colour = alive
                else:
                    colour = dead

                image.putpixel((x, y), colour)  # Place colour on image

        # Resize image
        new_size = self.size[0] * self.scale, self.size[1] * self.scale
        image = image.resize(new_size, Image.NEAREST)

        return image

    def __create_frames(self, colours: tuple[str, str], progress_bar: ChargingBar = None):

        """Creates images from grid values and stores them as frames."""

        for frame in self.grid.create_game():
            image = self.__create_image(frame, colours)
            self.frames.append(image)

            # Show progress
            if progress_bar:
                progress_bar.next()

    def export(self, colours: tuple[str, str] = DEFAULT_COLOURS):

        """Exports a GIF file of the game."""

        # Create frames showing progress
        if self.show_progress and not self.grid.continuous:
            with ChargingBar("Creating frames", max=self.grid.epochs) as bar:
                self.__create_frames(colours, bar)
            print("Saving GIF...")

        # Create frames without showing progress
        else:
            self.__create_frames(colours)  # Create the frames

        gif = self.frames[0]  # Grab the first image as the base
        gif.save(
            fp=FILENAME,
            format='GIF',
            append_images=self.frames,
            save_all=True,
            duration=self.frame_duration,
            loop=0
        )

        print(f"File {FILENAME} finished exporting.")
