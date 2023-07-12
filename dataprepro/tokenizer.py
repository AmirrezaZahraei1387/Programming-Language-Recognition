"""the tokenizer will tokenize the text into
it's words, and it will separate the names from
symbols used in the text.
for more imformations go to the
following url:
https://github.com/AmirrezaZahraei1387/text-similarity"""

import dataprepro.constants as constants


def tokenize(statement: str):
    tokenized_text = []
    maked_name = ""

    for word in statement:

        if word in constants.SYMBOLS:
            if maked_name != "":
                tokenized_text.append(maked_name)
                maked_name = ""
            tokenized_text.append(word)

        else:
            maked_name += word
    if maked_name != "":
        maked_name = maked_name.replace("\n", "")
        maked_name = maked_name.replace("\t", "")
        tokenized_text.append(maked_name)

    return tokenized_text


def generalformataddspace(tokenized_statement):
    statement = "S"
    word = []

    for element in tokenized_statement:

        if element in constants.SYMBOLS_:
            statement += element + "S"

        elif element != " ":

            statement += "NS"
            word.append(element)
    return statement, word