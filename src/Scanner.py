class Scanner:
    def __init__(self, folder_list):
        self.folder_list = folder_list
        self.duplicate_dict = {}

    def scan(self):
        print("Scanner started...\n")
        self.__walk_folders(self.folder_list)

    def __walk_folders(self, folder_list):
        for folder in folder_list:
            print("\t" + folder.path + " is scanning")
            self.__walk_files(folder)

    def __walk_files(self, folder):
        for file in folder.file_list:
            print("\t\t" + str(file) + " -> OK")
            self.__addToDictonary(file)
        if len(folder.subfolder_list) != 0:
            self.__walk_folders(folder.subfolder_list)

    def __addToDictonary(self, file):
        if file.hash not in self.duplicate_dict:
            duplicates = [file]
            self.duplicate_dict[file.hash] = duplicates
        else:
            self.duplicate_dict[file.hash].append(file)

    def printDuplicates(self):
        index = 1;
        for key, duplicate_list in self.duplicate_dict.items():
            if(len(duplicate_list) != 1):
                print(str(index) + " - ", end='')
                for file in duplicate_list:
                    print(file.path + ", ", end='')
                index += 1
                print("")
        print("\n\n\t\t" + str(index) + " duplicate found\n\n")
