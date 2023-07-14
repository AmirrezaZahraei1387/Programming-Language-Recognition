"""this is the program that will detect the language"""
from data_opener import DataFileOpener
from tokenizer import tokenize
from tokenizer import generalformataddspace
from prepro import open_file


def reco(code_lines: str):

    langs = []
    opener = DataFileOpener()

    for line in code_lines:
        tokens = tokenize(line)
        syntax = generalformataddspace(tokens)     # getting all the syntaxs in the tokenized statement
        lang = opener.search(syntax)
        langs.append(lang)


    return langs


a = ["""for i in range():"""]
b=reco(a)
print(b)


