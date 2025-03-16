import string
import random

def generator(text, sep=" ", option=None):
    if not isinstance(text, str) or not all(c in string.printable for c in text) or not isinstance(sep,str) or option not in [None, "shuffle", "unique", "ordered"]:
        yield "ERROR"
        return

    words = text.split(sep)

    if option == "shuffle":
        random.shuffle(words)
    elif option == "unique":
        words = list(set(words))
    elif option == "ordered":
        words.sort()

    for word in words:
        yield word
