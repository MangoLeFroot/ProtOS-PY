#!/usr/bin/env python3

__author__ = "Mango LeFroot"
__version__ = "0.1.0"
__license__ = "MIT"

import sys, signal
from rgbmatrix import RGBMatrix, RGBMatrixOptions

interrupt_received = False
def signal_handler(signal, frame):
    global interrupt_received
    interrupt_received = True


OptionsFace = None
MatrixFace = None


def setup():
    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGINT, signal_handler)

    #OptionsFace = RGBMatrixOptions()
    #OptionsFace.hardware_mapping = "adafruit-hat-pwm"
    #OptionsFace.cols = 64
    #OptionsFace.rows = 32
    #OptionsFace.chain_length = 2
    #OptionsFace.parallel = 1

    #OptionsFace.brightness = 80
    #OptionsFace.led_rgb_sequence = "BRG"
    #OptionsFace.limit_refresh_rate_hz = 90

    #MatrixFace = RGBMatrix(option = OptionsFace)

def loop():
    while not interrupt_received:
        print("Hello World!")

def main():
    setup()
    loop()
    sys.exit(0)

if __name__ == "__main__":
    main()