#!/usr/bin/env python

from time import sleep
from lib.display import Display


class SimulatorDisplay(Display):

    def __init__(self, x, y):
        Display.__init__(self, x, y)

    def off(self):
        pass

    def draw_buffer(self, buff):
        pass
