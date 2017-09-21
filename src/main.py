from src.Folder import Folder
from src.Scanner import Scanner
from src.DuplicateHandler import DuplicateHandler

folder = "/volumes/.../"
copy_destination = "/volumes/.../"

first_folder = Folder(folder)

scanner = Scanner([first_folder,])
scanner.scan()
scanner.printDuplicates()

handler = DuplicateHandler(scanner.duplicate_dict, copy_destination)
handler.start()
