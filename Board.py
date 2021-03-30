from Alphabet import *
from WordTree import *

class Board():

    SIZE = 15
    
    def __init__(self):
        self.array = [['|_' for _ in range(self.SIZE)] for _ in range(self.SIZE)]

    def validate_word(self, locations, dictionary, points):
        for location in locations:
            x_start_index, x_end_index = self.get_word_position(location)
            y_start_index, y_end_index = self.get_word_position([location[1], location[0]])
            word1 = self.get_word(x_start_index, x_end_index, location[1])
            word2 = self.get_word(y_start_index, y_end_index, location[0])
            if dictionary.contains(word1):
                points += calculate_word_points(word1)
            if dictionary.contains(word2):
                points += calculate_word_points(word2)
        return points
                
            


    def get_word(self, x1, x2, y):
        x = x1
        word = []
        for _ in range(x2-x1):
            word.append(self.array[x][y])
            x+=1
        return ''.join(word)

    def get_word_position(self, location):
        x = location[0]
        y = location[1]
        while self.array[x][y].isalpha():
            x -= 1
        x += 1
        x_start = x
        if x < Board.SIZE:
            while self.array[x][y].isalpha():
                if x < Board.SIZE:
                    x += 1
        x -= 1
        x_end = x

        return x_start, x_end                     # indexes

    def calculate_word_points(self, word):
        points = 0
        for letter in word:
            points += Alphabet.getpoints(letter)
        return points

    def update(self, plays, dictionary):
        """Takes in a tuple 3*(letter_object, xlocation, ylocation) and 
        updates Board() object and returns points"""
        points = 0
        locations = []
        for play in plays:
            letter = play[0]
            x = play[1]
            y = play[2]
            x_index = Alphabet.alphabet_string.index(x.upper())
            y_index = int(y)-1
            self.array[y_index][x_index] = f'|{letter.letter}'
            locations.append((x_index, y_index))
            points += int(letter.points)
        self.validate_word(locations, dictionary, points)
        return points

    def __str__(self):
        top =  '\n{:^34}'.format('~*SCRABBLE*~')+'\n   '+15*'_ '+'\n'
        bottom = '   '+' '.join(Alphabet.alphabet[_] for _ in range(self.SIZE))+'\n'
        return top+'\n'.join(['{:>2}'.format(_+1)+''.join(self.array[_])+'|' for _ in range(self.SIZE)])+'\n'+bottom

if __name__ == "__main__":
    b = Board()
    b.array[6][6] = '|K'
    print(b)