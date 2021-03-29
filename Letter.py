class Letter():
    def __init__(self, letter, points):
        self.letter = letter
        self.points = points

    def __add__(self, other):
        self.letter += other.letter
        self.points += other.points

    def __eq__(self, letter_string):
        return self.letter.upper() == letter_string.upper()

    def __str__(self):
        return self.letter