class DuplicateSet:
    set = []

    def has(self, file):
        for each_file in set:
            if each_file.path == file.path:
                return True
        return False