import os
import shutil
from_dir = "/Users/sappfamily/Downloads"
to_dir = "/Users/sappfamily/Desktop/Document_Files"
list_of_files = os.listdir(from_dir)
#print(list_of_files)
for file in list_of_files :
    name, extension = os.path.splitext(file)
    print(name)
    print(extension)