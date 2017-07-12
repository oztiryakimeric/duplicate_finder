from src.Folder import Folder
from src.Scanner import Scanner
from src.DuplicateHandler import DuplicateHandler

test_folder = "../test_folder"
test_folder_2 = "../test_folder_2"

folder = "/volumes/Adsız/resimler/"
copy_destination = "/volumes/Adsız/uni/"

first_folder = Folder(folder)

#print(first_folder)
#print(second_folder)

scanner = Scanner([first_folder,])
scanner.scan()
scanner.printDuplicates()

handler = DuplicateHandler(scanner.duplicate_dict, copy_destination)
handler.start()
