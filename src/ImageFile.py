import os, hashlib
from PIL import Image

class ImageFile:
    def __init__(self, path):
        self.path = path
        self.__errors = []
        self.img = Image.open(path)
        self.weight = self.__calculate_exif_weight()

    def __calculate_exif_weight(self):
        try:
            exif = self.img._getexif()
        except:
            return 0
        if exif == None: return 0

        weight = 0
        for k in exif:
            if exif[k] != "" or exif[k] != " " or exif[k] != None:
                weight += 1
        return weight;

    def get_exif_data(self):
        exif = self.img._getexif()
        if exif == None: return 0

        for k in exif:
            print(str(k) + " -> " + str(exif[k]), end=",")


    def __str__(self):
        return os.path.basename(self.path) + " - " + str(self.weight)

    def __eq__(self, other):
        return list(self.img.getdata()) == list(other.img.getdata())

    def hash(self):
        hash_obj = hashlib.sha512(self.img.tobytes())
        return hash_obj.hexdigest()
