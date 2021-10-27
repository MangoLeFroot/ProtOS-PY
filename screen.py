import os, json, numpy
from PIL import Image, ImageOps
from rgbmatrix import RGBMatrix
import rgbmatrix

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
            self.screenimage = imgfile.convert("RGB")
            imgfile.close()

    def update(self, matrix: RGBMatrix) -> RGBMatrix:

        matrix.SetImage(self.screenimage, self.config['position']['x'], self.config['position']['y'])
        if self.screeninfo['mirrored']:
            matrix.SetImage(ImageOps.mirror(self.screenimage), int(self.config['size']['width'] / 2) - 1 + self.config['position']['x'], self.config['position']['y'])        
            
        return matrix
