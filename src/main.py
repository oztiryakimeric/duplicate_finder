import os
import sys, getopt
from src.Folder import Folder
from src.Scanner import Scanner

test_folder = "../test_folder"
test_folder_2 = "../test_folder_2"

first_folder = Folder(test_folder)
second_folder = Folder(test_folder_2)

print(first_folder)
print(second_folder)

scanner = Scanner([first_folder, second_folder])
scanner.start()