#!/usr/bin/env python

# detect if running on RPi
try:
    import RPi as rpi
except ImportError:
    is_pi = False
else:
    del rpi
    is_pi = True

# get configuration
import config

# start color console logger
from lib.logor import Logor
Logor(config.LOGOR_FORMATS, config.LOGOR_LEVEL, config.LOGOR_COLOR_MAP)

if is_pi:
    from lib.gpio import Gpio
    from lib.display.rotating_display.cat4016 import Cat4016
    from lib.display.rotating_display import RotatingDisplay
    display = RotatingDisplay(
        config.DISPLAY_X,
        config.DISPLAY_Y,
        Gpio(config.ROTATING_DISPLAY_IR_ROTATION),
        Gpio(config.ROTATING_DISPLAY_MOTOR_DIRECTION),
        Cat4016(
            Gpio(config.CAT4016_CLOCK_PIN),
            Gpio(config.CAT4016_SIN_PIN),
            Gpio(config.CAT4016_LATCH_PIN),
            config.CAT4016_GROUPS,
            config.CAT4016_LED_MAP),
        config.ROTATING_DISPLAY_WRITE_RATE)
else:
    from lib.display.simulator_display import SimulatorDisplay
    display = SimulatorDisplay(
        config.DISPLAY_X,
        config.DISPLAY_Y)

modules = ["config", "lib.logor", "lib.display"]
if is_pi:
    modules += ["lib.gpio", "lib.display.rotating_display", "lib.display.rotating_display.cat4016"]
else:
    modules += ["lib.display.simulator_display"]
