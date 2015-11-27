from os import listdir
from os.path import isfile, join, isdir

def listDir(dir_path):
    if not isdir(dir_path):
        return None
    return [f for f in listdir(dir_path) if isfile(join(dir_path, f))]

def searchDir(dir_path):
    if not isdir(dir_path):
        return None
    return [with join(dir_path, f) as p
            for f in listdir(dir_path) if isfile(p))]
