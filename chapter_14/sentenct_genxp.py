import re
import reprlib

RE_WORD = '\w+'


class Sentence:

    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return 'Sentence{0}'.format(reprlib.repr(self.text))

    def __iter__(self):
        return (match.group() for match in RE_WORD.finditer(self.text))

