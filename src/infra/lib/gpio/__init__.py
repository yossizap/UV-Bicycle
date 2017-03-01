#!/usr/bin/env python

import logging

try:
    from RPi import GPIO as _GPIO
except RuntimeError:
    logging.error("Fail to import RPi.GPIO, run python as sudo!")
except ImportError:
    logging.error("Fail to import RPi.GPIO, code will not function as intended!")
    raise


class Gpio(object):
    OUTPUT_0 = False
    OUTPUT_1 = True
    INPUT_0 = _GPIO.PUD_DOWN
    INPUT_1 = _GPIO.PUD_UP
    RISING_EDGE = _GPIO.RISING
    FALLING_EDGE = _GPIO.FALLING
    _SETUP_ARGUMENTS = {
        OUTPUT_0: {"initial": OUTPUT_0},
        OUTPUT_1: {"initial": OUTPUT_1},
        INPUT_0: {"initial": OUTPUT_1},
    }
    _log = logging.getLogger()

    def __init__(self, pin, mode=INPUT_0):
        self._pin = -1 if pin is None else pin
        self._mode = mode

    def setup(self):
        _GPIO.setwarnings(False)
        _GPIO.setmode(_GPIO.BCM)
        self.set_mode()

    def write(self, value):
        _GPIO.output(self._pin, value)

    def set_mode(self, mode=None):
        if mode is not None:
            self._mode = mode
        if self._mode == self.OUTPUT_0 or self._mode == self.OUTPUT_1:
            _GPIO.setup(self._pin, _GPIO.OUT, initial=self._mode)
            self._log.debug("GPIO_%s mode: OUTPUT_%s", 1 if self._mode == self.OUTPUT_1 else 0)
        elif self._mode == self.INPUT_0 or self._mode == self.INPUT_1:
            _GPIO.setup(self._pin, _GPIO.IN, pull_up_down=self._mode)
            self._log.debug("GPIO_%s mode: INPUT_%s", 1 if self._mode == self.INPUT_1 else 0)
        else:
            self._log.error("Unknown GPIO mode: %s", self._mode)

    def pulse(self, is_high=True):
        self.write(is_high)
        self.write(not is_high)

    def cleanup(self):
        _GPIO.cleanup(self._pin)

    def __str__(self):
        return self._pin

    def __int__(self):
        return self._pin

if __name__ == "__main__":
    gpio = Gpio(**{})
