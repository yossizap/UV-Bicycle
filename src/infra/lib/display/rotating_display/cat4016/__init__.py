#!/usr/bin/env python

import logging
from lib.gpio import Gpio


class Cat4016(object):
    def __init__(self, clock_gpio, data_gpio, latch_gpio, groups, led_map):
        self._clock_gpio = clock_gpio
        self._data_gpio = data_gpio
        self._latch_gpio = latch_gpio
        self._gpios = (self._clock_gpio, self._data_gpio, self._latch_gpio)
        self._groups = groups
        self._led_map = led_map

    def setup(self):
        for gpio in self._gpios:
            gpio.set_mode(Gpio.OUTPUT_0)
        logging.info("Using GPIOs: data=%s, clock=%s, latch=%s", *self._gpios)

    def write(self, buffer):
        for led in self._led_map:
            self._data_gpio.write(False if led == -1 else buffer[led])
            for _ in range(self._groups):
                self._clock_gpio.pulse()
        self._latch_gpio.pulse()

    def cleanup(self):
        for gpio in self._gpios:
            gpio.cleanup()
        logging.info("GPIOs Released")
