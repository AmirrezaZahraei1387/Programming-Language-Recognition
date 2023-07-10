"""this is a class created for managing the paths
that are in  the data we have.
this important because there are a lot of data
and their path will become too messy easily"""

import constants
import pathlib
import os

def get_absolute_path(path):
    return pathlib.Path(path).absolute()


def get_all_absolute_path(names_elements, direct):

    pathspl = []
    for p in names_elements:
        pathspl.append(get_absolute_path(str(direct) + '/' + str(p)))
    return pathspl



supported_prog_langs = os.listdir(path_raw_data)  # we suppose for each programing
# language there is a directory with its name in the raw data
path_spl = get_all_absolute_path(supported_prog_langs, path_raw_data)
path_sub_spl = []

for p in path_spl:
    names = os.listdir(p)
    path_sub_spl.append(get_all_absolute_path(names, p))




class PathManager:

    def __init__(self, path_raw_data= constants.RAW_DATA_PATH, path_un_data= constants.UN_DATA_PATH):

        self.path_raw_data = get_absolute_path(path_raw_data)
        self.path_un_data = get_absolute_path(path_un_data)
        self.supported_prog_langs = os.listdir(self.path_raw_data)  # we assume that there are directories
        # in the raw data each with the name of the programing language
        # from now on spl means supported_programing_languages to avoid extra typings







