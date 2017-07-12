import shutil

class DuplicateHandler:
    def __init__(self, duplicate_dict, destination_folder):
        self.duplicate_dict = duplicate_dict
        self.destination_folder = destination_folder
        self.index = 0

    def start(self):
        for key in self.duplicate_dict:
            best = self.__find_best_file(self.duplicate_dict[key])
            self.copy(best)
            self.index += 1
        print("\n\n\t\t" + str(self.index) + " files copied\n\n")

    def __find_best_file(self, duplicate_list):
        max = None
        for file in duplicate_list:
            if not max or file.weight > max.weight:
                max = file
        return max

    def copy(self, file):
        print(str(self.index) + " - " + str(file))
        shutil.copy(file.path, self.destination_folder)


