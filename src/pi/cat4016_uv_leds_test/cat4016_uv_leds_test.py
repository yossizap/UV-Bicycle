#!/usr/bin/env python

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO! sudo?")
    raise

from time import sleep


LED_COUNT = 32
SIN_PIN = 22
CLOCK_PIN = 27
LATCH_PIN = 17


def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup((SIN_PIN, CLOCK_PIN, LATCH_PIN), GPIO.OUT)


def cleanup():
    GPIO.cleanup((SIN_PIN, CLOCK_PIN))


def pulse(pin):
    GPIO.output(pin, True)
    GPIO.output(pin, False)


def write(leds):
    for led in leds:
        GPIO.output(SIN_PIN, led)
        pulse(CLOCK_PIN)
    pulse(LATCH_PIN)


if __name__ == "__main__":
    setup()
    for i in xrange(LED_COUNT + 1):
        write([i == j for j in xrange(LED_COUNT)])
        time.sleep(0.2)
    cleanup()
