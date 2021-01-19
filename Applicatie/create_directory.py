import os
import shutil


def create_directory(files):
    current_dir = os.getcwd()
    new_directory = os.path.join(current_dir, r'current_files')
    if not os.path.exists(new_directory):
        os.makedirs(new_directory)

    add_files(files, new_directory)


def add_files(files, end_location):
    for x in files:
        print(open(x, 'r'))
        print(end_location + "\\" + x)
        shutil.move(x, end_location + "\\" + x)
