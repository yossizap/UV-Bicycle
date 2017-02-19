#!/usr/bin/env python

import os.path
from RPi import GPIO
from cat4016 import Cat4016
from graphics import Graphics
from rotating_display import RotatingDisplay


class Main(object):
    
    VERSION = 3
    if VERSION == 1:
        LED_COUNT = 32
        CAT4016_GROUPS = 1
        CAT4016_LED_MAP = range(LED_COUNT)
    elif VERSION == 2:
        LED_COUNT = 10
        CAT4016_GROUPS = 1
        CAT4016_LED_MAP = [-1 if i % 2 or i >= LED_COUNT * 2 else i / 2 for i in range(32)]
    elif VERSION == 3:
        LED_COUNT = 10
        CAT4016_GROUPS = 2
        CAT4016_LED_MAP = [0, -1, 2, 3, -1, 5, 6, 7, 8, 9, 4, 1, -1, -1, -1, -1]

    CAT4016_SIN_PIN = 22
    CAT4016_CLOCK_PIN = 27
    CAT4016_LATCH_PIN = 17
    IR_ROTATION_PIN = 0
    MOTOR_DIRACTION_PIN = 0
    TEST_BUTTON_PIN = 4

    def __init__(self):
        self.cat4016 = Cat4016(
            self.CAT4016_CLOCK_PIN,
            self.CAT4016_SIN_PIN,
            self.CAT4016_LATCH_PIN,
            self.CAT4016_GROUPS,
            self.CAT4016_LED_MAP)

        self.graphics = Graphics(self.LED_COUNT)

        self.rotating_display = RotatingDisplay(
            self.IR_ROTATION_PIN,
            self.MOTOR_DIRACTION_PIN,
            self.cat4016,
            self.graphics)

    def test_draw_images(self):
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "%s_pixels_high" % (self.LED_COUNT,))

        if os.path.isfile(image_path):
            images = [image_path]
        elif os.path.isdir(image_path):
            images = [os.path.join(image_path, i) for i in os.walk(image_path).next()[2]]
        else:
            raise Exception("the input is not a valid file or directory")

        for image in images * 100:
            self.rotating_display.draw_image(image)
            GPIO.wait_for_edge(self.TEST_BUTTON_PIN, GPIO.FALLING)

    def setup(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.TEST_BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        self.cat4016.setup()
        
    def cleanup(self):
        self.rotating_display.off()
        self.cat4016.cleanup()
        GPIO.cleanup()

if __name__ == "__main__":
    main = Main()
    main.setup()
    try:
        main.test_draw_images()
    finally:
        main.cleanup()
