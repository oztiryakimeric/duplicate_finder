import os
from src.ImageFile import ImageFile

class Folder:
    def __init__(self, path):
        print("Traversing " + path + "...")
        self.path = path
        self.file_list = []
        self.subfolder_list = []
        self.__errors = []
        self.__walk()

    def __walk(self):
        try:
            raw_folder_data = next(os.walk(self.path))
            self.__walk_folders(raw_folder_data[1])
            self.__walk_files(raw_folder_data[2])
        except StopIteration:
            pass

    def __walk_files(self, list):
        for file_name in list:
            image_file = self.__create_image_file(os.path.join(self.path, file_name))

            if image_file: self.file_list.append(image_file)

    def __walk_folders(self, list):
        for sub_dir in list:
            folder = Folder(os.path.join(self.path, sub_dir))
            self.subfolder_list.append(folder)

    def __create_image_file(self, path):
        try:
            return ImageFile(path)
        except OSError:
            self.__errors.append(os.path.basename(path) + " -> Not an image file.")
            return False

    def __write_errors(self):
        if len(self.__errors) != 0:
            if not os.path.exists("errors"):
                os.makedirs("errors")
            error_file = open("errors/" + self.path.replace("/", "_") + ".txt", "w")
            error_file.writelines(self.__errors)
            error_file.close()

    def __print(self, path, file_list, indent_level):
        if indent_level <= 2: text = str(path) + ":\n"
        else: text = "\t"*(indent_level-2) + "|-" + str(path) + ":\n"

        for file in file_list:
            text += "\t"*indent_level + "|-" + str(file) + "\n"
        return text

    def __str__(self):
        text = self.__print(self.path, self.file_list, 1)

        indent_counter = 2
        for folder in self.subfolder_list:
            text += "\t" + "|-" + self.__print(folder.path, folder.file_list, indent_counter)
            indent_counter += 1
        return text