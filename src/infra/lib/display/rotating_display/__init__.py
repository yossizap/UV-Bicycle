#!/usr/bin/env python

from time import sleep
from lib.display import Display


class RotatingDisplay(Display):

    def __init__(self, x, y, ir_rotation_gpio, motor_direction_gpio, leds_driver, write_rate):
        self._ir_rotation_gpio = ir_rotation_gpio
        self._motor_direction_gpio = motor_direction_gpio
        self._leds_driver = leds_driver
        self._write_rate = write_rate
        Display.__init__(self, x, y)

    def off(self):
        self._leds_driver.write([False] * self._y)

    def draw_buffer(self, buff):
        for i in buff:
            self._leds_driver.write(i)
            sleep(self._write_rate)
        self.off()
