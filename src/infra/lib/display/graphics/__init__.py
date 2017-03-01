#!/usr/bin/env python

from PIL import Image


class Graphics(object):

    @staticmethod
    def image_to_buffer(image_path, inverted=True):
        image = Image.open(image_path).convert("L")
        w, h = image.size
        return [[inverted ^ bool(image.getpixel((x, y))) for y in xrange(h)] for x in xrange(w)]

    @staticmethod
    def text_to_buffer(text, font, x, y, h):
        pass
