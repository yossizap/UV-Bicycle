#!/usr/bin/env python

import logging
from lib.ansi import Ansi


LOGOR_LEVEL = logging.DEBUG
LOGOR_FORMATS = ("%(asctime)s %(name)s %(levelname)s:\n%(message)s", "%d/%m/%y %H:%M:%S")
LOGOR_COLOR_MAP = {
    logging.CRITICAL: (Ansi.YELLOW, Ansi.BACKGROUND_RED,),
    logging.ERROR: (Ansi.RED, Ansi.BRIGHT),
    logging.WARNING: (Ansi.YELLOW, Ansi.BRIGHT),
    logging.INFO: (Ansi.CYAN, Ansi.FAINT),
    logging.DEBUG: (Ansi.YELLOW, Ansi.FAINT),
    "name": (Ansi.GREEN, Ansi.FAINT),
    "levelname": (Ansi.MAGENTA, Ansi.FAINT),
}

INTERACTIVE_SHELL_EMBED_ARGUMENTS = {
    "banner1": Ansi.style(
r"""
                  /'\
                 /
                /                 ,
             c-'                 /
            /'-._         ,____,' .-'''-.
       .-'.// \  '-;-========,"-,'       '
     ,`   /,   \_//\       ,/  (  '- *)   )
    (   ./  )   {,}========'===='- '     ,
     ,     ,   \/               ',      .
 _____'-.-`_______________________'-..-'____

  U V   B i c y c l e   I n t e r f a c e:
____________________________________________
""", Ansi.CYAN, Ansi.BRIGHT),
    "confirm_exit": False,
    "exit_msg": "Bye :)",
}

CAT4016_CLOCK_PIN = 27
CAT4016_SIN_PIN = 22
CAT4016_LATCH_PIN = 17

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

DISPLAY_X = 100
DISPLAY_Y = LED_COUNT

ROTATING_DISPLAY_IR_ROTATION = None
ROTATING_DISPLAY_MOTOR_DIRECTION = None
ROTATING_DISPLAY_WRITE_RATE = 0.2


Sentences = [
    u"Hello World",
    u"UV-Bicycle",
    u"jerusalem science museum",
]
