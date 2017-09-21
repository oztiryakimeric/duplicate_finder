import os, hashlib
from PIL import Image
import imagehash

class ImageFile:
    def __init__(self, path):
        self.path = path
        self.__errors = []
        temp_img = self.get_img()
        self.hash = self.__calculate_hash(temp_img)
        self.weight = self.__calculate_exif_weight(temp_img)

    def __calculate_exif_weight(self, img):
        try:
            exif = img._getexif()
        except:
            return 0
        if exif is None:
            return 0

        weight = 0
        for k in exif:
            if exif[k] != "" or exif[k] != " " or exif[k] != None:
                weight += 1
        return weight;

    def __calculate_hash(self, img):
        return imagehash.average_hash(img)

    def get_img(self):
        return Image.open(self.path)

    def __str__(self):
        return os.path.basename(self.path) + " - " + str(self.weight)



