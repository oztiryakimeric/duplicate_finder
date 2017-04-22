import os
from PIL import Image

class ImageFile:

    def __init__(self, path):
        self.path = path
        self.__errors = []
        self.img = Image.open(path)

    def __str__(self):
        return os.path.basename(self.path)

    def __eq__(self, other):
        return list(self.img.getdata()) == list(other.img.getdata())