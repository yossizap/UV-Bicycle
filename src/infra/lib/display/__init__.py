#!/usr/bin/env python

from lib.display.graphics import Graphics


class Display(object):

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def draw_buffer(self, buff):
        raise NotImplementedError()

    def draw_image(self, image_path, inverted=True):
        self.draw_buffer(Graphics.image_to_buffer(image_path, inverted))

    def draw_text(self, text, font, x, y, h):
        self.draw_buffer(Graphics.text_to_buffer(text, font, x, y, h))
