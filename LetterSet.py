import random
from Letter import *
from Alphabet import *

class LetterSet(Alphabet):

    SIZE = 7

    def __init__(self):
        Alphabet.__init__(self)
        self.letter_set = []
        for _ in range(LetterSet.SIZE):
            index = random.randint(0, self.size-1)
            self.letter_set.append(self.alphabet(index))

    def __str__(self):
        letters = '\t'.join([letter.letter for letter in self.letter_set])
        points = '\t'.join([letter.points for letter in self.letter_set])
        return f'{letters}\n{points}'