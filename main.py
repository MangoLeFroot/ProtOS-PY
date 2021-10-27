#!/usr/bin/env python3

__author__ = "Mango LeFroot"
__version__ = "0.1.0"
__license__ = "MIT"

import screen
import server

import sys, signal
from rgbmatrix import RGBMatrix, RGBMatrixOptions

class App:
    """ Root application for proto nonesense """
    def __init__(self) -> None:
        self.OptionsFace = None
        self.MatrixFace = None
        self.CanvasFace = None

        self.setup_face()


    def setup_face(self):
        """ Set up the face matrix """
        self.OptionsFace = RGBMatrixOptions()
        self.OptionsFace.hardware_mapping = "adafruit-hat"
        self.OptionsFace.cols = 64
        self.OptionsFace.rows = 32
        self.OptionsFace.chain_length = 2
        self.OptionsFace.parallel = 1

        self.OptionsFace.brightness = 80
        self.OptionsFace.led_rgb_sequence = "BRG"
        self.OptionsFace.limit_refresh_rate_hz = 90

        self.MatrixFace = RGBMatrix(options = self.OptionsFace)
        self.CanvasFace = self.MatrixFace.CreateFrameCanvas()

        self.face = screen.Screen()
        self.face.load_config("config", "faces.json")
        self.face.set_screeninfo("default")

    def update(self):
        self.CanvasFace = self.face.update(self.CanvasFace)

    def draw(self):
        self.CanvasFace = self.MatrixFace.SwapOnVSync(self.CanvasFace)

    def destroy(self):
        self.MatrixFace.Clear()


interrupt_received = False
def signal_handler(signal, frame):
    global interrupt_received
    interrupt_received = True

def main():
    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGINT, signal_handler)

    app = App()
    #server.start()

    while not interrupt_received:
        app.update()
        app.draw()

    app.destroy()
    sys.exit(0)

if __name__ == "__main__":
    main()
