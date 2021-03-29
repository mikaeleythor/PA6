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
    	    # letter = self.letters[counter]
            letter = self.letters[counter]
            if letter_string == letter:
                found = True
                return letter
            else:
                counter += 1
            if counter == LetterSet.SIZE-1:                 # Avoiding IndexError
                break

    def get_valid_letter(self, _):
        letter_string = input(f'Choose letter {_+1}: ')
        if self.letters.contains(letter_string):
            return letter_string
        else:
            print('Invalid letter!\n')
            return self.get_valid_letter(_)

    def update_letterset(self):
        pass

    def get_valid_location(self, _):
        location_list = list(input(f'Choose a location {_+1}(e.g. G10): '))
        if location_list[0].isalpha():
            if location_list[-1].isnumeric():
                if len(location_list) < 4:
                    if len(location_list) > 1:
                        temp_list = location_list[:]
                        temp_list.pop(0)
                        if int(''.join(temp_list)) < 16:
                            return location_list

        print('Invalid location!\n')
        return self.get_valid_location(_)


    def play(self):
        """This function prompts for a letter_string and location 
        and returns a tuple: 3*(letter_object, xlocation, ylocation)"""
        plays = []
        for _ in range(3):
            letter_string = self.get_valid_letter(_)
            letter = self.choose_letter(letter_string)
            location_list = self.get_valid_location(_)
            x = location_list.pop(0)
            y = int(''.join(location_list))
            plays.append((letter, x, y))
        return plays

if __name__ == "__main__":
    P = Player()
    print(P)