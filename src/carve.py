"""
Used to remove lowest energy seam from an image. Used iteratively
to reduce the size of the image horizontially by one pixel each
iteration.
"""

import sys

from energy import compute_energy
from seam import compute_vertical_seam, visualize_seam_on_image
from utils import Color, read_image_into_array, write_array_into_image


def remove_seam_from_image(image, seam_xs):
    """
    Removes the seam from the given image. X-coordiantes are specified from
    top to bottom and span the image horizontally.
    """
    
    m_grid = [ [p for x, p in enumerate(row) if x != seam_xs[y]] for (y, row) in enumerate(image)]

    return m_grid 


def remove_n_lowest_seams_from_image(image, num_seams_to_remove):
    """
    Iteratively finds the lowest energy seam in the image and removes it.

    Returns the image after seams are removed
    """

    for i in range(num_seams_to_remove):
        print(f'Removing seam {i + 1}/{num_seams_to_remove}')
        
        print('Computing energy...')
        energy_data = compute_energy(image)
        print('Finding the lowest-energy seam...')
        seam_xs, min_seam_energy = compute_vertical_seam(energy_data)
        print('Removing lowest energy seam from image...')
        image = remove_seam_from_image(image, seam_xs) 

    return image

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print(f'USAGE: {__file__} <input> <num-seams-to-remove> <output>')
        sys.exit(1)

    input_filename = sys.argv[1]
    num_seams_to_remove = int(sys.argv[2])
    output_filename = sys.argv[3]

    print(f'Reading {input_filename}...')
    pixels = read_image_into_array(input_filename)

    print(f'Saving {output_filename}')
    resized_pixels = \
        remove_n_lowest_seams_from_image(pixels, num_seams_to_remove)
    write_array_into_image(resized_pixels, output_filename)
