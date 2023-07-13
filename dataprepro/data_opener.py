"""for managing the data better we created this program
to open the data for us. it can make every thing very better
because we won't get messy in the main file."""

import os
import pathlib
import dataprepro.path_manager as path_manager
import dataprepro.constants as constants


class DataFileOpener:

    def __init__(self):
        obj = path_manager.PathManager(constants.RAW_DATA_PATH, constants.UN_DATA_PATH)
        self.path = obj.path_un_data
        self.supported_langs = os.listdir(self.path)

    def make_path(self, lang):
        """this method wil make the path of data.txt by getting a language"""


        if lang not in self.supported_langs:
            raise NotImplementedError("the lang expected is not implemented")
        return str(self.path)+str("/")+lang+"/"+"data.txt"

    def open_langs(self, lang):
        """opening the data using a language"""
        with open(self.make_path(lang), mode="r") as file:
            data = eval(file.read())
        file.close()
        return data

    def open_number(self, num):
        """opening the data using numbers"""
        return self.open_langs(self.supported_langs[num])
