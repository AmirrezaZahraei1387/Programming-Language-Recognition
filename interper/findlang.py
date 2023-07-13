"""this is the program that will detect the language"""
from dataprepro.data_opener import DataFileOpener
from dataprepro.tokenizer import tokenize
from dataprepro.tokenizer import generalformataddspace
from dataprepro import open_file


def reco(code_lines: str):

    opener = DataFileOpener()

    for line in code_lines:
        tokens = tokenize(line)
        syntaxs = generalformataddspace(tokens)     # getting all the syntaxs in the tokenized statement








