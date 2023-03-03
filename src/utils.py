"""
Utilities to work with images.
"""

from PIL import Image

class Color:
    """
    Class representing an RGB value.
    """

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __str__(self):
        return f'Color({self.r}, {self.g}, {self.b})'

def read_image_into_array(filename):
    """
    Read the given image into a 2D array of pixels.
    Each row is an array of Color objects.

    Returns the 2D array
    """

    img = Image.open(filename, 'r')
    w, h = img.size

    pixels = list(Color(*pixel) for pixel in img.getdata())
    return [pixels[n:(n + w)] for n in range(0, w * h, w)]

def write_array_into_image(pixels, filename):
    """
    Write the given 2D array of pixels into an image with the given filename.
    """

    h = len(pixels)
    w = len(pixels[0])

    img = Image.new('RGB', (w, h))

    output_pixels = img.load()
    for y, row in enumerate(pixels):
        for x, color in enumerate(row):
            output_pixels[x, y] = (color.r, color.g, color.b)

    img.save(filename)
