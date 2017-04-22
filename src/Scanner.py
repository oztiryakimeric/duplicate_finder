class Scanner:
    def __init__(self, folder_list):
        self.folder_list = folder_list

    def start(self):
        print("Scanner started...")
        self.__traverse_files(self.folder_list[0])

    def __traverse_files(self, folder):
        for file in folder.file_list:
            scan_result = self.__scan(file, folder)
            if(scan_result): print("Duplicate found for: " + str(file) + " -> " + str(scan_result))
            else: print("No duplicate for " + str(file))

        if(len(folder.subfolder_list) == 0): return
        else:
            for subfolder in folder.subfolder_list:
                self.__traverse_files(subfolder)

    def __scan(self, file, folder):
        duplicate = folder.has_duplicate_of(file)
        if duplicate: return duplicate

        if len(folder.subfolder_list) == 0: return
        else:
            self.__scan(file, folder.subfolder_list)
