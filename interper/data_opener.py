"""for managing the data better we created this program
to open the data for us. it can make every thing very better
because we won't get messy in the main file."""

import os
import pathlib


class DataFileOpener:

    def __init__(self, path=constants.DAtA_FILE):

        self.supported_langs = os.listdir(self.path)

    def make_path(self, lang):
        """this method wil make the path of data.txt by getting a language"""

        if lang not in self.supported_langs:
            raise NotImplementedError("the lang expected is not implemented")
        return self.path+str("/")+lang+"/"+"data.txt"

    def open_langs(self, lang):
        """opening the data using a language"""
        with open(self.make_path(lang), mode="r") as file:
            data = list(file.read())
        file.close()
        return data

    def open_number(self, num):
        """opening the data using numbers"""
        return self.open_langs(self.supported_langs[num])


a = DataFileOpener()


