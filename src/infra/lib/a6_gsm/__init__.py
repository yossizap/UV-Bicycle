#!/usr/bin/env python

import logging
from lib.gpio import Gpio
from serial import Serial


class A6Gsm(object):

    def __init__(self, port, power_gpio=None):
        self._port = port
        self._power_gpio = power_gpio
        self._serial = Serial()

    def set_pwoer(self, is_on):
        if self._power_gpio == self._port:
            if self._serial.is_open:
                self._serial.setDTR(is_on)
        elif self._power_gpio is not None:
            self._power_gpio.write(is_on)
        else:
            return
        # sleep

    def setup(self):
        self._serial = Serial(self._port)
        self.set_pwoer(True)

    def read_serial(self):
        return self._serial.read_until()

    def recv_loop(self):
        while True:
            pass
