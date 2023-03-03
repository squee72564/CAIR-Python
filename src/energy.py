"""
Used to compute the energy of the image. Can be used without
carving functionality to produce a heatmap of the image.
"""

import sys

from utils import Color, read_image_into_array, write_array_into_image

def energy_at(pixels, x, y):
    """
    Computes the energy at a single pixel at position (x, y) of image.

    Energy of a pixel is defined by the change in color of the surrounding pixels
    relative to the pixel passed in the function.

    Returns a number representing the energy the pixel at that point.
    """

    w = len(pixels[0])
    h = len(pixels)

    x0 = x if x == 0 else x-1
    x1= x if x == w-1 else x+1

    y0 = y if y == 0 else y-1
    y1 = y if y == h-1 else y+1

    delta_x = (pixels[y][x0].r - pixels[y][x1].r)**2 + (pixels[y][x0].g - pixels[y][x1].g)**2 + (pixels[y][x0].b - pixels[y][x1].b)**2

    delta_y = (pixels[y0][x].r - pixels[y1][x].r)**2 +  (pixels[y0][x].g - pixels[y1][x].g)**2 +  (pixels[y0][x].b - pixels[y1][x].b)**2 

    return delta_x + delta_y

def compute_energy(pixels):
    """
    Computes energy of image at every pixel. Uses energy_at function to
    compute energy at single position.

    The input is given as 2D array of colors

    Output is a 2D array of numbers representing the energy calue at each
    corresponding postition.
    """

    energyGrid = []

    w = len(pixels[0])
    h = len(pixels)

    for y in range(h):
        pixelRow = []
        for x in range(w):
            pixelRow.append(energy_at(pixels, x , y))
        energyGrid.append(pixelRow)

    return energyGrid

def energy_data_to_colors(energy_data):
    """
    Convert the energy values at each pixel into colors that can be used to
    visualize the energy of the image. The steps to do this conversion are:

      1. Normalize the energy values to be between 0 and 255.
      2. Convert these values into grayscale colors, where the RGB values are
         all the same for a single color.
    """

    colors = [[0 for _ in row] for row in energy_data]

    max_energy = max(
        energy
        for row in energy_data
        for energy in row
    )

    for y, row in enumerate(energy_data):
        for x, energy in enumerate(row):
            energy_normalized = round(energy / max_energy * 255)
            colors[y][x] = Color(
                energy_normalized,
                energy_normalized,
                energy_normalized
            )

    return colors

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f'USAGE: {__file__} <input> <output>')
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    print(f'Reading {input_filename}...')
    pixels = read_image_into_array(input_filename)

    print('Computing the energy...')
    energy_data = compute_energy(pixels)
    energy_pixels = energy_data_to_colors(energy_data)

    print(f'Saving {output_filename}')
    write_array_into_image(energy_pixels, output_filename)
