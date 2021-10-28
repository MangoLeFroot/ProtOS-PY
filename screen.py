import os, json, numpy
from PIL import Image, ImageOps
from rgbmatrix import RGBMatrix
import rgbmatrix

class Screen:
    def __init__(self) -> None:
        self.config = None
        self.screeninfo = None

        self.screenimage = None
        self.screenduration = None

        self.n_frame = 0
        self.max_frame = 0
        self.elapsed_time = 0

    def load_config(self, path: str, file_name: str):
        conffile = os.path.join(path, file_name)
        
        with open(conffile, 'r') as jsonfile:
            self.config = json.load(jsonfile)
            jsonfile.close()

    def set_screeninfo(self, name: str):
        self.screeninfo = self.config[name]

        with Image.open(self.screeninfo['path'], 'r')  as imgfile:
            self.screenimage = []
            self.screenduration = []
            self.n_frame = 7

            if hasattr(imgfile, "n_frames"):
                for i in range(imgfile.n_frames):
                    imgfile.seek(i)
                    self.screenduration.append(imgfile.info['duration'])
                    self.screenimage.append(imgfile.convert("RGB"))
                    if self.screeninfo['color']:
                        self.screenimage[i] = Image.composite((self.screeninfo['color']['r'], self.screeninfo['color']['g'], self.screeninfo['color']['b']), self.screenimage[i], self.screenimage[i].convert("L"))
            else:
                self.screenimage.append(imgfile.convert("RGB"))
                if self.screeninfo['color']:
                    self.screenimage[0] = Image.composite((self.screeninfo['color']['r'], self.screeninfo['color']['g'], self.screeninfo['color']['b']), self.screenimage[0], self.screenimage[0].convert("L"))

            self.max_frame = len(self.screenimage)
            imgfile.close()

    def update(self, matrix: RGBMatrix, deltaTime: int) -> RGBMatrix:
        self.elapsed_time = self.elapsed_time + deltaTime
        if self.elapsed_time >= self.screenduration[self.n_frame]:
            self.n_frame = self.n_frame + 1
            self.elapsed_time = 0

        if self.n_frame == self.max_frame:
            self.n_frame = 0

        matrix.SetImage(self.screenimage[self.n_frame], self.config['position']['x'], self.config['position']['y'])
        if self.screeninfo['mirrored']:
            matrix.SetImage(ImageOps.mirror(self.screenimage[self.n_frame]), int(self.config['size']['width'] / 2) + self.config['position']['x'], self.config['position']['y'])      

        return matrix
