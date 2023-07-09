"""this is the file that the data preprocessing will be
donne here. so basically we upload all the files then we
extract the syntax, and then we write into the un-data folder"""
import os
import pathlib
import constants

path_un_data = pathlib.Path(constants.UN_DATA_PATH).absolute()
path_raw_data = pathlib.Path(constants.RAW_DATA_PATH).absolute()  # resolving the path and getting
# the correct path
supported_prog_langs = os.listdir(path_raw_data)  # we suppose for each programing
# language there is a directory with its name in the raw data




