import re
from constants import (SEPARATORS, NON_DECLARATIVE_SEPARATORS,
                       WORD, NUMBER, ABBREVIATION, ABBREVIATION_TWO_WORDS)


def amount_of_sentences(str_):
    str_ = str_.lower()  #заменяет большие буквы на маленькие
    amount = len(re.findall(SEPARATORS, str_))

    for i in ABBREVIATION:
        amount -= str_.count(i)

    for i in ABBREVIATION_TWO_WORDS:
        amount -= 2 * str_.count(i)

    return amount


def amount_of_non_declarative_sentences(str_):
    amount = len(re.findall(NON_DECLARATIVE_SEPARATORS, str_))

    return amount


def average_length_of_sentences(str_):
    numbers_re = re.findall(NUMBER, str_)
    words_re = re.findall(WORD, str_)
    words = []

    for i in words_re:
        if i not in numbers_re:
            words.append(i)

    sentences_len_in_characters = 0

    for i in words:
        sentences_len_in_characters += len(i)

    amount = amount_of_sentences(str_)
    if amount != 0:
        average_len_sentences = sentences_len_in_characters / amount
        return round(average_len_sentences, 2)
    else:
        return 0


