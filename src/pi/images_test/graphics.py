#!/usr/bin/env python

from PIL import Image


class Graphics(object):

    def __init__(self, leds_count):
        self._leds_count = leds_count

    def image_to_buffer(self, image_path, inverted=True):
        image = Image.open(image_path).convert("L")
        w, h = image.size
        if h != self._leds_count:
            raise Exception("Image height doesn't match led count: %s != %s" % (h, self._leds_count))
        return [[inverted ^ bool(image.getpixel((x, y))) for y in xrange(h)] for x in xrange(w)]    

    def text_to_buffer(self, text, font, x, y, h):
        pass
