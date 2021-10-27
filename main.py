#!/usr/bin/env python3

__author__ = "Mango LeFroot"
__version__ = "0.1.0"
__license__ = "MIT"

import screen
import server

import sys, signal, time
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
        self.OptionsFace.hardware_mapping = "adafruit-hat-pwm"
        self.OptionsFace.cols = 64
        self.OptionsFace.rows = 32
        self.OptionsFace.chain_length = 2
        self.OptionsFace.parallel = 1

        self.OptionsFace.brightness = 80
        self.OptionsFace.led_rgb_sequence = "BRG"
        self.OptionsFace.limit_refresh_rate_hz = 90
        #self.OptionsFace.show_refresh_rate = True

        #self.OptionsFace.gpio_slowdown = 0
        #self.OptionsFace.pwm_dither_bits = 1
        #self.OptionsFace.pwm_lsb_nanoseconds = 50
        #self.OptionsFace.pwm_bits = 7

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
        #start_time = time.time()
        app.update()
        app.draw()
        #print("FPS: ", 1.0 / (time.time() - start_time)) # FPS = 1 / time to process loop

    app.destroy()
    sys.exit(0)

if __name__ == "__main__":
    main()
