# Conway
[![License: MIT](https://img.shields.io/badge/License-MIT-black.svg)](https://opensource.org/licenses/MIT)
### Matteo Golin
A Pythonic recreation of Conway's game of life using classic rules for cell implementation. Games are
exported as black and white GIFs.

## Usage
Create a grid object initialized with a seed, and then pass it to the GIFExporter object along with the
number of epochs you want the game to run for.

Run the `.export()` method on the exporter and your game will be visible in the `animation.gif` file.

## Requirements
- Python 3.9.2 greater
- Pillow module
- Progress module
