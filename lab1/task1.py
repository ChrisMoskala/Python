import os, sys


def countFiles(dir):
    try:
        directory = os.listdir(dir)
    except FileNotFoundError:
        print("directory " + dir + " does not exists")
        sys.exit()
    noFiles = 0
    for name in directory:
        if os.path.isfile(os.path.join(dir, name)):
            noFiles += 1
    print("in " + dir + " directorty there is " + str(noFiles) + " files")


countFiles("C:/Users/arekk/Desktop/doc")
