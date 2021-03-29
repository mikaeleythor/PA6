from Alphabet import *

class Board():

    SIZE = 15
    
    def __init__(self):
        self.array = [['|_' for _ in range(self.SIZE)] for _ in range(self.SIZE)]

    def board_formatting(self):
        pass

    def insert_letter(self):
        pass

    def update(self, plays):
        """Takes in a tuple 3*(letter_object, xlocation, ylocation) and 
        updates Board() object and returns points"""
        points = 0
        for play in plays:
            letter = play[0]
            points += int(letter.points)
            x = play[1]
            y = play[2]
            x_index = Alphabet.alphabet_string.index(x)
            y_index = int(y)-1
            self.array[x_index][y_index] = letter
        return points

    def __str__(self):
        top =  '\n{:^34}'.format('~*SCRABBLE*~')+'\n   '+15*'_ '+'\n'
        bottom = '   '+' '.join(Alphabet.alphabet[_] for _ in range(self.SIZE))+'\n'
        return top+'\n'.join(['{:>2}'.format(_+1)+''.join(self.array[_])+'|' for _ in range(self.SIZE)])+'\n'+bottom

if __name__ == "__main__":
    b = Board()
    b.array[6][6] = '|K'
    print(b)