#!/usr/bin/env python

try:
    from RPi import GPIO
except RuntimeError:
    print("Error importing RPi.GPIO! sudo?")


class Cat4016(object):
    def __init__(self, clock_pin, data_pin, latch_pin, groups, led_map):
        self._clock_pin = clock_pin
        self._data_pin = data_pin
        self._latch_pin = latch_pin
        self._groups = groups
        self._led_map = led_map

    def setup(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup((self._data_pin, self._clock_pin, self._latch_pin), GPIO.OUT)

    def _gpio_pulse(self, gpio_pin):
        GPIO.output(gpio_pin, True)
        GPIO.output(gpio_pin, False)

    def write(self, buffer):
        for led in self._led_map:
            GPIO.output(self._data_pin, False if led == -1 else buffer[led])
            for _ in range(self._groups):
                self._gpio_pulse(self._clock_pin)
        self._gpio_pulse(self._latch_pin)

    def cleanup(self):
        GPIO.cleanup((self._data_pin, self._clock_pin))
