"""this is the file that the data preprocessing will be
donne here. so basically we upload all the files then we
extract the syntax, and then we write into the un-data folder"""
import os
import pathlib
import constants


def get_absolute_path(path):
    return pathlib.Path(path).absolute()


path_un_data = get_absolute_path(constants.UN_DATA_PATH)
path_raw_data = get_absolute_path(constants.RAW_DATA_PATH)  # resolving the path and getting
# the correct path
supported_prog_langs = os.listdir(path_raw_data)  # we suppose for each programing
# language there is a directory with its name in the raw data
path_spl = []

for path in supported_prog_langs:
    path_spl.append(get_absolute_path(str(path_raw_data)+'/'+str(path)))

print(path_spl)