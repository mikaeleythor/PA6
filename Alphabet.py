from Letter import *

class Alphabet():
    letter_list_object = open("english_alphabet.txt")
    point_list_object = open("english_alphabet_points.txt")
    alphabet_string = letter_list_object.read()
    points = point_list_object.read()
    alphabet = list(alphabet_string)
    points = points.split()

    def __init__(self):
        self.letters = [Letter(Alphabet.alphabet[_], Alphabet.points[_]) for _ in range(len(Alphabet.alphabet))]
        self.length = len(Alphabet.alphabet)

    def __getitem__(self, index):
        return self.letters[index]

    def getpoints(letter):
        index = Alphabet.alphabet.index('letter')
        letter_object = self.letters[index]
        return letter_object.points


if __name__ == "__main__":
    A = Alphabet()
    letter_string = 'e'
    print(A.alphabet_string)
    # print(A.get_index(letter_string))