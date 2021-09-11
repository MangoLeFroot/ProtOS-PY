#!/usr/bin/env python3

__author__ = "Mango LeFroot"
__version__ = "0.1.0"
__license__ = "MIT"

from PIL import Image
from PIL import ImageDraw
import time
from rgbmatrix import RGBMatrix, RGBMatrixOptions

OptionsFace = None
MatrixFace = None


def setup():
    OptionsFace = RGBMatrixOptions()
    OptionsFace.hardware_mapping = "adafruit-hat-pwm"
    OptionsFace.cols = 64
    OptionsFace.rows = 32
    OptionsFace.chain_length = 2
    OptionsFace.parallel = 1

    OptionsFace.brightness = 80
    OptionsFace.led_rgb_sequence = "BRG"
    OptionsFace.limit_refresh_rate_hz = 90

    MatrixFace = RGBMatrix(option = OptionsFace)

def loop():
    print("hello world")

def main():
    setup()
    loop()


if __name__ == "__main__":
    main()