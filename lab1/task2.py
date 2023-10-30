import os, sys


def listFiles(dir):
    try:
        directory = os.listdir(dir)
    except FileNotFoundError:
        print("directory " + dir + " does not exists")
        sys.exit()
    res = []
    for dir_path, dirs, file_names in os.walk(dir):
        res.extend(file_names)
        print(str(dir_path) + "" + str(dirs) + "" + str(file_names) + "\n")


listFiles("C:/Users/arekk/Desktop/doc")
