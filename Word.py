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

    def __len__(self):
        return len(self.word)

    def __lt__(self, word):
        if len(word) < len(self.word):
            short_word = word
            other_word = self.word
        else:
            short_word = self.word
            other_word = word
        for index, letter in enumerate(short_word):
            if letter < other_word[index]:
                return True
            elif letter > other_word[index]:
                return False
        if short_word == self.word:
            return True
        elif self.word == word:
            return False