from itertools import groupby


def word_counter(*words):
    '''Write a Python program that inputs a list of words, separated by white-
    space, and outputs how many times each word appears in the list. You
    need not worry about efficiency at this point, however, as this topic is
    something that will be addressed later in this book.
    '''
    return {word: len(list(word_group)) for word, word_group in
            groupby(sorted(words, key=lambda x: x), key=lambda x: x)}
