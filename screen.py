import os, json, numpy
from PIL import Image
from rgbmatrix import FrameCanvas

class Screen:
    def __init__(self) -> None:
        self.config = None
        self.screeninfo = None
        self.screenimage = None

    def load_config(self, path: str, file_name: str):
        conffile = os.path.join(path, file_name)
        
        with open(conffile, 'r') as jsonfile:
            self.config = json.load(jsonfile)
            jsonfile.close()

    def set_screeninfo(self, name: str):
        self.screeninfo = self.config[name]

        with Image.open(self.screeninfo['path'], 'r')  as imgfile:
            self.screenimage = numpy.array(imgfile.convert("RGB"))
            imgfile.close()

    def update(self, canvas: FrameCanvas) -> FrameCanvas:

        if self.screeninfo['mirrored']:
            for y in range(0, self.config['size']['height'] - 1):
                for x in range(0, int(self.config['size']['width'] / 2) - 1):
                    pixel = self.screenimage[y][x]
                    canvas.SetPixel(self.config['position']['x'] + x,
                                    self.config['position']['y'] + y,
                                    pixel[0],
                                    pixel[1],
                                    pixel[2])

                    canvas.SetPixel((self.config['size']['width'] + int(self.config['size']['width'] / 2) - 1) - (self.config['position']['x'] + x + int(self.config['size']['width'] / 2)),
                                    self.config['position']['y'] + y,
                                    pixel[0],
                                    pixel[1],
                                    pixel[2])
        
        return canvas
