class Letter():
    def __init__(self, letter, points):
        self.letter = letter
        self.points = points

    def __add__(self, other):
        self.letter += other.letter
        self.points += other.points