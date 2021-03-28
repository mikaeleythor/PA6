from Word import *
from WordTree import *
from LetterSet import *
from Player import *

def read_file(filename):
    file_object = open(filename)
    line_list = file_object.readlines()
    return line_list[2::]

def get_attributes(line_list):
    """This function extracts wanted values from each line in line_list"""
    word_list = []
    for line in line_list:
        temp = line.split()
        word = temp.pop(0)
        keys = temp.pop(-1)
        language = ''
        word2 = ''
        try:
            if temp[1].isupper():
                word2 = temp.pop(1)
                if temp[2][0] == '(':
                    language = temp.pop(2)
            elif temp[1][0] == '(':
                language = temp.pop(1)    
        except IndexError: # If IndexError occurs then values language and word2 do not exist
            pass
        definition = ' '.join(temp)
        word_list.append((Word(word, word2, language, keys, definition)))
    return word_list

def create_dictionary():
    line_list = read_file('Collins Scrabble Words (2019) with definitions.txt')
    word_list = get_attributes(line_list)
    word_tree = WordTree()
    for word in word_list:
        word_tree.insert(word)    
    return word_tree
if __name__ == "__main__":
    dictionary = create_dictionary()
    # player1, player2 = Player(), Player()