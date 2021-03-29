import random
from Letter import *
from Alphabet import *

class LetterSet(Alphabet):

    SIZE = 7

    def __init__(self):
        Alphabet.__init__(self)
        self.letter_set = []
        for _ in range(LetterSet.SIZE):
            index = random.randint(0, self.length-1)
            self.letter_set.append(self.letters[index])

    def __str__(self):
        letters = '|\t|'.join([str(letter.letter) for letter in self.letter_set])
        points = '|\t|'.join([str(letter.points) for letter in self.letter_set])
        return f'|{letters}|\n|{points}|'

    def __getitem__(self, index):
        return self.letter_set[index]



if __name__ == "__main__":
    L = LetterSet()
    print(L)
