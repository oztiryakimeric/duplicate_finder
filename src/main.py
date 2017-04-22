import os
import sys, getopt
from src.Folder import Folder
from src.Scanner import Scanner

test_folder = "test_folder"
test_folder_2 = "test_folder_2"
hdd_path = "/volumes/adsız/camera_uploads"
google_drive = "/users/oztiryakimeric/googledrive/other"

first_folder = Folder(test_folder)

print(first_folder)

scanner = Scanner([first_folder,])
scanner.start()