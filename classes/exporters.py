# Holds the exporter classes for the simulation
__author__ = "Matteo Golin"

# Imports
from PIL import Image, ImageColor
from progress.bar import Bar
from classes.grid import Grid
from customtypes import GridField, Simulation
from typing import Protocol

# Constants
Palette = tuple[str, str]
Size = tuple[int, int]
DEFAULT_COLOURS: Palette = "#222323", "#f0f6f0"


# Helper functions
def _create_image(generation: GridField, colours: Palette, size: Size, scale: int) -> Image:
    """Returns an image based on the passed grid snapshot."""

    # Unpack size
    cols, rows = size

    # Unpack colours
    dead, alive = colours
    dead, alive = ImageColor.getrgb(dead), ImageColor.getrgb(alive)

    image = Image.new('RGB', size, dead)  # Define image

    for y in range(rows):  # Rows
        for x in range(cols):  # Columns
            current_cell = generation[y][x]

            # Decide on colour
            if current_cell.alive:
                image.putpixel((x, y), alive)  # Place colour on image

    # Resize image
    new_size = cols * scale, rows * scale
    image = image.resize(new_size, Image.NEAREST)

    return image


def _create_images(colours: Palette, simulation: Simulation, size: Size, scale: int, step_size: int = 1,
                   progress_bar: Bar = None) -> list[Image]:
    """
    Returns a list of images, recorded on every snapshot which is a multiple of the step size parameter.
    Progress is shown via a progress bar if one is provided.
    Default step_size is 1, which records an image every frame.
    """

    images: list[Image] = []
    counter = 0

    for generation in simulation:
        if counter % step_size == 0:

            # Store images
            image = _create_image(generation=generation, colours=colours, size=size, scale=scale)
            images.append(image)

            # Show progress
            if progress_bar:
                progress_bar.next()

        counter += 1

    return images


# Classes
class Exporter(Protocol):
    """An object that exports some type of visualization of a simulation via an export method."""

    def export(self, filepath: str, colours: Palette = DEFAULT_COLOURS) -> None:
        """Exports the simulation in some media format using two colours to the specified pathway."""
        ...


class ImageExporter:
    """
    Exports the simulation generations every multiple of the step size as an image file. Uses PNG as the default image
    type.
    """

    def __init__(self, grid: Grid, scale: int, step_size: int):
        self.grid: Grid = grid
        self.scale: int = scale
        self.size: Size = grid.columns, grid.rows
        self.step_size: int = step_size
        self.__extension: str = "png"

    @property
    def extension(self) -> str:
        """Sets the extension/file type for the image file."""
        return self.__extension

    @extension.setter
    def extension(self, extension: str) -> None:
        """Sets the extension/file type for the image file."""

        # Check if the extension is valid and implemented
        if extension.lower() not in ["jpg", "jpeg", "png"]:
            raise ValueError(f"The image extension '{extension.lower()}' is not a valid or implemented extension.")

        self.__extension = extension.lower()

    def export(self, filepath: str, colours: Palette = DEFAULT_COLOURS) -> None:
        """
        Exports simulation generations every multiple of the step size as an image file with the desired filepath and
        colours.
        """

        # Decide whether to show progress
        if not self.grid.continuous:
            bar = Bar("Creating images", max=(self.grid.epochs // self.step_size))
        else:
            bar = None

        images = _create_images(
            colours,
            simulation=self.grid.create_simulation(),
            size=self.size,
            scale=self.scale,
            step_size=self.step_size,
            progress_bar=bar
        )

        # Finish the progress bar if it was used
        if bar:
            bar.finish()

        # Save the images
        with Bar("Saving images", max=len(images)) as bar:
            for num, image in enumerate(images):
                image.save(f"{filepath}_{num + 1}.{self.extension}")
                bar.next()


class GIFExporter:
    """Exports simulation generations as a GIF animation with the desired frame duration."""

    def __init__(self, grid: Grid, scale: int, frame_duration: int):
        self.grid: Grid = grid
        self.scale: int = scale
        self.size: Size = grid.columns, grid.rows
        self.frame_duration: int = frame_duration

    def export(self, filepath: str, colours: Palette = DEFAULT_COLOURS) -> None:
        """Exports simulation generations every multiple of the step size as a GIF file."""

        # Decide whether to show progress
        if not self.grid.continuous:
            bar = Bar("Creating frames", max=self.grid.epochs)
        else:
            bar = None

        frames = _create_images(
            colours,
            simulation=self.grid.create_simulation(),
            size=self.size,
            scale=self.scale,
            progress_bar=bar
        )

        # Finish the progress bar if it was used
        if bar:
            bar.finish()

            # Save the GIF animation
        gif = frames.pop(0)  # Grab the first image as the base
        gif.save(
            fp=f"{filepath}.gif",
            format='GIF',
            append_images=frames,
            save_all=True,
            duration=self.frame_duration,
            loop=0
        )
