from LetterSet import *

class Player():

    number = 0

    def __init__(self):
        Player.number += 1
        self.name = input(f'Enter username for player {Player.number}: ')
        self.letters = LetterSet()
        self.points = 0