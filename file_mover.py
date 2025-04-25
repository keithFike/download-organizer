#! /usr/bin/python3

import os
import pathlib


def getFileExtension(file):
    file_extension = pathlib.Path(file).suffix

    return file_extension

def updateFileDict(file_dict, file, extension):
    file_dict.update({file:extension})

def createDirectory(file_dict):
    for file, extension in file_dict.items():
        if extension.strip(".") not in os.listdir(os.getcwd()):
            try:
                os.mkdir(extension.strip(".") + "_files")
            except FileExistsError:
                print(f"Directory for {file}:{extension} already exists")

def moveFile(file_dict):
    for file, extension in file_dict.items():
        os.rename(file, extension.strip(".") + "_files" + "/" + file)

def main():
    file_dict = {}

    os.chdir('directory here')

    current_files = os.listdir(os.getcwd())

    for file in current_files:
        if os.path.isdir(file) != True:
            updateFileDict(file_dict, file, getFileExtension(file))

    createDirectory(file_dict)
    moveFile(file_dict)

if __name__ == "__main__":
    main()
