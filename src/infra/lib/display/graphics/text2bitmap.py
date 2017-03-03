'''
Description: Converts a given text to a BMP file
Requirements: Pillow
'''

import PIL
import PIL.Image
import PIL.ImageFont
import PIL.ImageOps
import PIL.ImageDraw
from optparse import OptionParser

PIL_GREYSCALE = "L"
DEFAULT_FONT = "arial.ttf"
DEFAULT_FONT_SIZE = 10

def points_to_pixels(points):
    """
    Converts the given number of points(PIL's representation of size) to pixels
    """
    return int(round(points * 1.333333))
    
def pixels_to_points(pixels):
    """
    Converts the given number of pixels to points
    """
    return int(round(pixels * 0.75))
    
def text_to_image(string, font_path, font_size):
    """
    Convert a given string to a grey-scale image
    """
    try:
        font = PIL.ImageFont.truetype(font_path, font_size)
    except IOError:
        font = PIL.ImageFont.load_default()
        print('Could not use chosen font. Using default.')

    height = points_to_pixels(font.getsize(string)[1])
    width = points_to_pixels(font.getsize(string)[0])

    image = PIL.Image.new(PIL_GREYSCALE, (width, height), "white")
    draw = PIL.ImageDraw.Draw(image)

    draw.text((5, 5), string, "black", font)
    c_box = PIL.ImageOps.invert(image).getbbox()
    image = image.crop(c_box)
    return image
    
def main():
    parser = OptionParser()
    parser.add_option("-s", "--string", dest="string", help="String to convert")
    parser.add_option("-f", "--font", dest="font", help="Font name/path")
    parser.add_option("-o", "--output_path", dest="output_path", help="Output path for the resulting image")
    parser.add_option("-S", "--font_size", dest="size", help="The size of the font in points")
    
    (options, args) = parser.parse_args()
    
    if not options.string:
        print "A valid string must be provided, please read --help"
        return
        
    if not options.output_path:
        print "A valid output path must be provided, please read --help"
        return
        
    if options.size:
        size = int(options.size)
    else:
        size = DEFAULT_FONT_SIZE
        
    image = text_to_image(unicode(options.string), options.font or DEFAULT_FONT, pixels_to_points(size))
    image.save(options.output_path)
    
if __name__ == '__main__':
    main()