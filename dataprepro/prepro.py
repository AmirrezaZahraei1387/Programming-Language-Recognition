"""this is the file that the data preprocessing will be
donne here. so basically we upload all the files then we
extract the syntax, and then we write into the un-data folder"""

import os
import dataprepro.tokenizer as tokenizer
import dataprepro.path_manager as path_manager
import dataprepro.constants as constants


def open_file(path):
    with open(file=path, encoding="utf-8", mode="r") as data_file:
        data = data_file.readlines()
    data_file.close()
    return data


def search(array, item):
    index = -1
    for element in array:
        index += 1
        if element[0] == item:
            return index


def is_empty(folder):
    """this method will remove the files and folders under a
    directory"""

    files = os.listdir(folder)
    if not files:
        return True
    return False


def main_prog(un_data, raw_data):
    """the un_data is empty folder for the program result
    and raw data is the data is going to be processed"""
    program_path = path_manager.PathManager(raw_data, un_data)

    index = -1

    for lang in program_path.supported_prog_langs:

        index += 1

        tokenized_texts = []

        for path_raw_data in program_path.path_sub_spl[index]:

            data = open_file(path_raw_data)

            for statement in data:
                if statement != "\n" or statement != "":  # checking if the line is empty or no

                    t = tokenizer.tokenize(statement[:-1])
                    result = tokenizer.generalformataddspace(t)
                    search_result = search(tokenized_texts, result[0])  # it can be none or the index of the object

                    if search_result is None:
                        tokenized_texts.append([result[0], [result[1]]])

                    else:
                        tokenized_texts[search_result][1].append(result[1])

        # here the work for that language is done, and so
        # we go to do another one that exist

        path_new = program_path.new_path_under_dir(program_path.path_un_data, lang)
        os.mkdir(path_new)

        path_text_file = program_path.new_path_under_dir(path_new, "data.txt")

        with open(path_text_file, "a") as file:
            file.write(str(tokenized_texts))
        file.close()


main_prog(constants.UN_DATA_PATH, constants.RAW_DATA_PATH)






