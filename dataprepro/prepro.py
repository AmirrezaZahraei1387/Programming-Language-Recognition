"""this is the file that the data preprocessing will be
donne here. so basically we upload all the files then we
extract the syntax, and then we write into the un-data folder"""

import os
import sys
import tokenizer
import path_manager


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


def remove_files(folder):
    """this method will remove the files and folders under a
    directory"""

    files = os.listdir(folder)
    if files:
        for pa in files:
            try:
                os.remove(program_path.new_path_under_dir(folder, pa))
            except IsADirectoryError:
                os.rmdir(program_path.new_path_under_dir(folder, pa))


program_path = path_manager.PathManager()


def main_prog():
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


def main():

    try:
        remove_files(program_path.path_un_data)
    except PermissionError:
        print("there are some files in the un-data while it is expected to be empty. please clean it manually"
              "because we can't do that")
        sys.exit()
    main_prog()
















