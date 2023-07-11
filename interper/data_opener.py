"""for managing the data better we created this program
to open the data for us. it can make every thing very better
because we won't get messy in the main file."""

import interper.constants as constants
import os


class DataFileOpener:

    def __init__(self, path=constants.DAtA_FILE):
        self.path = path
        self.supported_langs = os.listdir(self.path)

    def make_path(self, lang):
        """this method wil make the path of data.txt by getting a language"""

        if lang not in self.supported_langs:
            raise NotImplementedError("the lang expected is not implemented")
        return self.path+str("/")+lang+"/"+"data.txt"

    def open_langs(self, lang):
        pass






