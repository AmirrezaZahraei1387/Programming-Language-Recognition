"""this is the program that will detect the language"""
from data_opener import DataFileOpener
from tokenizer import tokenize
from tokenizer import generalformataddspace
from dataprepro import open_file


def reco(code_lines: str):

    opener = DataFileOpener()

    for line in code_lines:
        tokens = tokenize(line)
        syntaxs = generalformataddspace(tokens)     # getting all the syntaxs in the tokenized statement








