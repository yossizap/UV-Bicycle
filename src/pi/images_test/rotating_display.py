#!/usr/bin/env python

from time import sleep


class RotatingDisplay(object):

    SLEEP = 0.2

    def __init__(self, ir_rotation_pin, motor_diraction_pin, leds_driver, graphics):
        self._ir_rotation_pin = ir_rotation_pin
        self._motor_diraction_pin = motor_diraction_pin
        self._leds_driver = leds_driver
        self._graphics = graphics

    def off(self):
        self._leds_driver.write([False] * self._graphics._leds_count)

    def draw_buffer(self, buffer):
        for i in buffer:
            self._leds_driver.write(i)
            sleep(self.SLEEP)
        self.off()
        
    def draw_image(self, image_path, inverted=True):
        self.draw_buffer(self._graphics.image_to_buffer(image_path, inverted))

    def draw_text(self, text, font, x, y, h):
        self.draw_buffer(self._graphics.text_to_buffer(text, font, x, y, h))
