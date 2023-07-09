"""this is the file that the data preprocessing will be
donne here. so basically we upload all the files then we
extract the syntax, and then we write into the un-data folder"""
import os
import pathlib
import constants


def get_absolute_path(path):
    return pathlib.Path(path).absolute()


def get_all_absolute_path(names_elements, direct):

    pathspl = []
    for p in names_elements:
        pathspl.append(get_absolute_path(str(direct) + '/' + str(p)))
    return pathspl


# uploading all the needed paths to work with
path_un_data = get_absolute_path(constants.UN_DATA_PATH)
path_raw_data = get_absolute_path(constants.RAW_DATA_PATH)  # resolving the path and getting
# the correct path
supported_prog_langs = os.listdir(path_raw_data)  # we suppose for each programing
# language there is a directory with its name in the raw data
path_spl = get_all_absolute_path(supported_prog_langs, path_raw_data)
path_sub_spl = []
for p in path_spl:
    names = os.listdir(p)
    path_sub_spl.append(get_all_absolute_path(names, p))

print("path_un_data:", path_un_data)
print("path_raw_data:", path_raw_data)
print("supported_prog_langs:", supported_prog_langs)
print("path_spl:", path_spl)
print("path_sub_spl", path_sub_spl)
# ===============================================











