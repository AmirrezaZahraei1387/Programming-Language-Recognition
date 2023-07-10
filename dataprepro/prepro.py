"""this is the file that the data preprocessing will be
donne here. so basically we upload all the files then we
extract the syntax, and then we write into the un-data folder"""

import os
import pathlib
import constants
import tokenizer


def get_absolute_path(path):
    return pathlib.Path(path).absolute()


def get_all_absolute_path(names_elements, direct):

    pathspl = []
    for p in names_elements:
        pathspl.append(get_absolute_path(str(direct) + '/' + str(p)))
    return pathspl


def open_file(path):

    with open(file= path, encoding= "utf-8", mode="r") as data_file:
        data = data_file.readlines()
    data_file.close()
    return data


def search(array, item):

    index = -1
    for element in array:
        index += 1
        if element[0] == item:
            return index


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

index = -1

for lang in supported_prog_langs:

    index += 1
    path_new = get_absolute_path(str(path_un_data)+'/'+str(lang))
    os.mkdir(path_new)
    tokenized_texts = []
    print("programing language:", lang)
    for path_raw_data in path_sub_spl[index]:

        data = open_file(path_raw_data)

        for statement in data:
            if statement != "\n" or statement != "":    # checking if the line is empty or no

                t = tokenizer.tokenize(statement[:-1])
                result = tokenizer.generalformataddspace(t)
                search_result = search(tokenized_texts, result[0])  # it can be none or the index of the object

                if search_result is None:
                    tokenized_texts.append([result[0],[result[1]]])

                else:
                    tokenized_texts[search_result][1].append(result[1])

    # here the work for that language is done, and so
    # we go to do another one that exist

    path_text_file = get_absolute_path(str(path_new)+"/"+"data.txt")
    with open(path_text_file, "a") as file:
        file.write(str(tokenized_texts))
    file.close()

















