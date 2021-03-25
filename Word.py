from Letter import *

class Word():

    def __init__(self, word, word2, word_type, language, definition):
        self.word = word
        self.word2 = word2
        self.language = language
        self.type = word_type
        self.definition = definition

    def __getitem__(self, index):
        return self.word[index]

    def __lt__(self, other):
        for index, letter in enumerate(self.word):
            if letter < other.word[index]:
                return True
            elif letter > other.word[index]:
                return False
        if len(self.word) < len(other.word):
            return True
        elif self.word == other.word:
            return False