"""
File: codeinplace_filter.py
----------------
This program implements a rad image filter.
"""

from simpleimage import SimpleImage

DEFAULT_FILE = 'images/lizshoeing.jpg'

def main():
    # Get file and load image
    filename = get_file()
    image = SimpleImage(filename)

    # Show the image before transforming
    image.show()

    # Show the image after transforming
    codeinplace_image = codeinplace_filter(filename)
    codeinplace_image.show()

# Apply the filter
def codeinplace_filter(filename):
    image = SimpleImage(filename)
    for pixel in image:
        pixel.red *= 1.5
        pixel.green *= .7
        pixel.blue *= 1.5
    return image

def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename


if __name__ == '__main__':
    main()
