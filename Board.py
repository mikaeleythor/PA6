from Alphabet import *

class Board():

    SIZE = 15
    
    def __init__(self):
        self.array = [['|_' for _ in range(self.SIZE)] for _ in range(self.SIZE)]

    def board_formatting(self):
        pass

    def __str__(self):
        top =  '{:^34}'.format('~*SCRABBLE*~')+'\n   '+15*'_ '+'\n'
        bottom = '   '+' '.join(Alphabet.alphabet[_] for _ in range(self.SIZE))
        return top+'\n'.join(['{:>2}'.format(_+1)+''.join(self.array[_])+'|' for _ in range(self.SIZE)])+'\n'+bottom

if __name__ == "__main__":
    b = Board()
    print(b)