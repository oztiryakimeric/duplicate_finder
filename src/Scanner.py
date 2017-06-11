class Scanner:
    def __init__(self, folder_list):
        self.folder_list = folder_list
        self.duplicate_list = []

    def start(self):
        print("Scanner started...")
        for folder in self.folder_list:
            self.traverse_all_files(folder)
        print(self.duplicate_list)

    def traverse_all_files(self, folder):
        for file in folder.file_list:
            print("\tSearching for file: " + str(file))
            self.search_for(file)
            self.__line()
        for subfolder in folder.subfolder_list:
            self.traverse_all_files(subfolder)

    def search_for(self, file):
        for parent_folder in self.folder_list:
            search_results = parent_folder.has_duplicate_of(file)
            if search_results:
                print("\t\t\t\t" + str(len(search_results)) + " duplicates found in current folder.")
                for result in search_results:
                    if(self.__is_result_stored(file)):
                        self.duplicate_list = [result]
                    else:
                        self.duplicate_list.append(result)

    def __line(self):
        print("\t" + "-" * 75)