from LetterSet import *

class Player():

    number = 0

    def __init__(self):
        Player.number += 1
        self.name = input(f'Enter username for player {Player.number}: ')
        self.letters = LetterSet()
        self.points = 0

    def __str__(self):
        spacing = ' _\t'
        return f'Your move {self.name}:\n{7*spacing}\n{self.letters}'

    def choose_letter(self, letter_string):
        found = False
        counter = 0
        while not found:
    	    letter = self.letters[counter]
            if letter_string == letter:
                found = True
                return letter
            else:
                counter += 1
            if counter == LetterSet.SIZE-1:                 # Avoiding IndexError
                break

    def play(self):
        """This function prompts for a letter_string and location 
        and returns a tuple: 3*(letter_object, xlocation, ylocation)"""
        plays = []
        for _ in range(3):
            letter_string = input('Choose a letter: ')
            letter = self.choose_letter(letter_string)
            location_list = list(input('Choose a location (e.g. G10): '))
            x = location_list.pop(0)
            y = int(''.join(location_list))
            plays.append((letter, x, y))
        return plays

if __name__ == "__main__":
    P = Player()
    print(P)