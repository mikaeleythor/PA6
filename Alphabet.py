from Letter import *

class Alphabet():
    letter_list_object = open("english_alphabet.txt")
    point_list_object = open("english_alphabet_points.txt")
    alphabet = letter_list_object.read()
    points = point_list_object.read()
    alphabet = list(alphabet)
    points = points.split()

    def __init__(self):
        self.letters = [Letter(alphabet[_], points[_]) for _ in range(len(alphabet))]
        self.length = len(self.alphabet)

    def __getitem__(self, index):
        return self.letters[index]